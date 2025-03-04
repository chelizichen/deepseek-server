from langchain_deepseek import ChatDeepSeekAI
from ai import config
llm = ChatDeepSeekAI(
    model="deepseek-chat",
    temperature=2,
    max_retries=2,
    api_key=config.conf.get("api_key"),
)

messages = [
    ("system", "你是一名全栈开发者，精通Nodejs、Python、Vue、Mysql"),
]


def ai_programmer(req: str):
    messages.append(("human", req))
    stream = llm.stream(messages)
    full = next(stream)
    print("******** ANSWER START *******")
    for chunk in stream:
        full += chunk
        print(chunk)
    print("******** ANSWER END *******")
    messages.append(("system", full.content))
    return full
