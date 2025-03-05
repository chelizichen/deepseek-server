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


def ai_programmer(req_question: str, prompts=None, isInit=False):
    if isInit:
        messages = []
        messages.append(("system", f"你是一名AI人工智能体，目前赋予你的标签是 {prompts}"))
        messages.append(("human", req_question))
        stream = llm.stream(messages)
        full = next(stream)
        for chunk in stream:
            full += chunk
        res_answer = full.content
        return {
            "answer": res_answer,
            "question": req_question,
        }
    else:
        messages = []
