from langchain_deepseek import ChatDeepSeekAI
from storage.storage import add_chat, get_chat
from conf import sgrid_config

api_key = sgrid_config.get("config.api_key")
print("api_key", api_key)

llm = ChatDeepSeekAI(
    model="deepseek-chat",
    temperature=2,
    max_retries=2,
    api_key=api_key,
)


def process_messages_and_stream(llm, messages):
    stream = llm.stream(messages)
    full = next(stream)
    for chunk in stream:
        full += chunk
    res_answer = full.content
    return res_answer


def chat_service(req_question: str, prompts: list, is_init=False, history=None):
    prompts_tag = ""
    for prompt in prompts:
        prompts_tag += "[" + prompt.get("prompt_name") + "] "

    messages = [("system", f"你是一名AI人工智能体，目前赋予你的标签是 {prompts_tag}")]
    if is_init:
        messages.append(("human", req_question))
    else:
        for chat in history:
            messages.append(("human", chat.question))
            messages.append(("ai", chat.answer))
        messages.append(("human", req_question))
        print(" chat_service >>  messages ", messages)
    res_answer = process_messages_and_stream(llm, messages)

    return {
        "answer": res_answer,
        "question": req_question,
    }
