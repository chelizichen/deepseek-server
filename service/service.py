from datetime import datetime

from langchain_deepseek import ChatDeepSeekAI

from application import const
from storage.dto import ChatDTO
from storage.storage import add_chat, get_chat
from conf import sgrid_application
from typing_extensions import Union

api_key = sgrid_application.get("config.api_key")
print("api_key", api_key)

llm = ChatDeepSeekAI(
    model="deepseek-chat",
    temperature=2,
    max_retries=2,
    api_key=api_key,
)


def process_messages_and_stream(llm_service, messages):
    stream = llm_service.stream(messages)
    full = next(stream)
    for chunk in stream:
        full += chunk
    res_answer = full.content
    return res_answer


def chat_service(req_question: str, prompts: list, is_init=False, history=Union[list, None]):
    prompts_tag = ""
    for prompt in prompts:
        prompts_tag += "[" + prompt.get("prompt_name") + "] "
    print(" chat_service >>  prompts_tag ", prompts_tag)
    print(" chat_service >>  history ", history)
    messages = [("system", f"你是一名AI人工智能体，目前赋予你的标签是 {prompts_tag}")]
    if is_init:
        messages.append(("human", req_question))
    else:
        if history is not None and isinstance(history, list):
            for chat in history:
                messages.append(("human", chat.get("question")))
                messages.append(("ai", chat.get("answer")))
            messages.append(("human", req_question))
    print(" chat_service >>  messages ", messages)
    res_answer = process_messages_and_stream(llm, messages)

    return {
        "answer": res_answer,
        "question": req_question,
    }

def create_abstract(data:ChatDTO):
    chat_type = data.chat_type
    print("chat_type:", chat_type)
    if chat_type is not None and chat_type is const.chat_type_abstract:
        print("invoke >> create abstract ")
        prompts = data.prompts
        if prompts is None:
            prompts = []
        history = data.history
        chat_rsp = chat_service(data.chat_msg, prompts, False, history)
        answer = chat_rsp.get("answer")
        question = chat_rsp.get("question")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_chat(
            data.user_id,
            question,
            answer,
            const.chat_type_abstract,
            const.answer_type_like,
            now,
            data.session_id
        )
        return