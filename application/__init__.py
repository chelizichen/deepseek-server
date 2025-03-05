from datetime import datetime

from application.const import new_uuid
from service.service import chat_service
from fastapi import FastAPI
from storage.storage import add_user, get_chat_history_by_session_id, get_prompts_by_session_id, add_chat, add_session, \
    add_prompt, add_chat_prompt
from application import const
import uuid

app = FastAPI()


@app.get("/greet")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(data: dict):
    uuid = new_uuid()
    """
    1. 首次进来，通过提示词进行初始化聊天
    2. 非首次进来，通过聊天记录拼接上下文进行聊天
    """
    chat_msg = data.get("chat_msg")
    session_id = data.get("session_id")
    user_id = data.get("user_id")

    print(f"invoke [chat] {uuid} >> chat_msg  {chat_msg} | session_id {session_id} | user_id {user_id}")
    history = get_chat_history_by_session_id(session_id)
    print(f"history {uuid} >>  {history}")
    prompts = get_prompts_by_session_id(session_id)
    print(f"prompts {uuid} >>  {prompts}")
    is_init = len(history) == 0
    print(f"is_init {uuid} >>  {is_init}")
    if is_init:
        chat_rsp = chat_service(chat_msg, prompts, True)
    else:
        chat_rsp = chat_service(chat_msg, prompts, False, history)
    answer = chat_rsp.get("answer")
    question = chat_rsp.get("question")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_chat(
        user_id,
        question,
        answer,
        const.chat_type_common,
        const.answer_type_common,
        now,
        session_id
    )
    return chat_rsp


@app.post("/sessions/save")
async def save_session(data: dict):
    # 从传入的 JSON 数据中提取所需信息
    user_id = data.get("user_id")
    name = data.get("name")
    print(f"invoke >> save_session | user_id {user_id} | name {name}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_info = add_session(user_id, name, now)
    return add_info


@app.post("/prompts/save")
async def save_prompts(data: dict):
    user_id = data.get("user_id")
    name = data.get("name")
    print(f"invoke >> save_prompts | user_id {user_id} | name {name}")
    # 从传入的 JSON 数据中提取所需信息
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt = add_prompt(name, 0, user_id, now)
    return prompt

@app.post("/chat_prompts/save")
async def save_prompts(data: dict):
    session_id = data.get("session_id")
    user_id = data.get("user_id")
    prompt_id = data.get("prompt_id")
    print(f"invoke >> save_prompts | session_id {session_id} | prompt_id {prompt_id} | user_id {user_id}")
    prompt = add_chat_prompt(session_id, user_id,prompt_id)
    return prompt


@app.get("/test/save")
async def test_save():
    user = add_user("John Doe11", "john@example.com")
    return user
