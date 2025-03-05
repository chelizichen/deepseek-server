from langchain_deepseek import ChatDeepSeekAI

from conf.init import sgrid_config

api_key = sgrid_config.get("config.api_key")
print("api_key", api_key)

llm = ChatDeepSeekAI(
    model="deepseek-chat",
    temperature=2,
    max_retries=2,
    api_key=api_key,
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
        print(chunk.content)
    print("******** ANSWER END *******")
    messages.append(("system", full.content))
    return full
