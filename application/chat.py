from storage.storage import add_user, get_chat_history_by_session_id, get_prompts_by_session_id, add_chat, add_session, \
    add_prompt, add_chat_prompt, get_sessions_by_user_id, update_chat
from datetime import datetime
from service.service import chat_service
from application.const import new_uuid
import application.const as const
from utils import wrap_response


def create_chat_router(app):
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
        chat_type = data.get("chat_type")
        if chat_type is not None:
            if chat_type == const.chat_type_abstract:
                prompts = data.get("prompts")
                history = data.get("history")
                chat_rsp = chat_service(chat_msg, prompts, False, history)
                answer = chat_rsp.get("answer")
                question = chat_rsp.get("question")
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                add_chat(
                    user_id,
                    question,
                    answer,
                    const.chat_type_abstract,
                    const.answer_type_like,
                    now,
                    session_id
                )
                return

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

        # 生成摘要
        history.reverse()
        type_list = []
        for his_chat in history:
            if his_chat.type == const.chat_type_abstract:
                break
            type_list.append(his_chat.type)
        history.reverse()
        # 如果当前聊天记录大于3条，则生成摘要
        print(f" {uuid} type_list length {len(type_list)}")
        if len(type_list) >= 3:
            print(f" {uuid} create abstract")
            abstract_req = dict()
            abstract_req["chat_type"] = const.chat_type_abstract
            abstract_req["chat_msg"] = "请将上述的内容进行总结"
            abstract_req["user_id"] = data.get("user_id")
            abstract_req["session_id"] = data.get("session_id")
            abstract_req["history"] = history
            abstract_req["prompts"] = prompts
            await chat(abstract_req)
            return wrap_response(chat_rsp)
        return wrap_response(chat_rsp)

    @app.get("/get_chat_history")
    def get_chat_history(session_id: int):
        # 从数据库中获取聊天记录
        chat_history = get_chat_history_by_session_id(session_id)
        return wrap_response(chat_history)

    @app.post("/sessions/save")
    async def save_session(data: dict):
        # 从传入的 JSON 数据中提取所需信息
        user_id = data.get("user_id")
        name = data.get("name")
        print(f"invoke >> save_session | user_id {user_id} | name {name}")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_info = add_session(user_id, name, now)
        return wrap_response(add_info)

    @app.post("/prompts/save")
    async def save_prompts(data: dict):
        user_id = data.get("user_id")
        name = data.get("name")
        print(f"invoke >> save_prompts | user_id {user_id} | name {name}")
        # 从传入的 JSON 数据中提取所需信息
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prompt = add_prompt(name, 0, user_id, now)
        return wrap_response(prompt)

    @app.post("/chat_prompts/save")
    async def save_prompts(data: dict):
        session_id = data.get("session_id")
        user_id = data.get("user_id")
        prompt_id = data.get("prompt_id")
        print(f"invoke >> save_prompts | session_id {session_id} | prompt_id {prompt_id} | user_id {user_id}")
        prompt = add_chat_prompt(session_id, user_id, prompt_id)
        return wrap_response(prompt)

    @app.get("/users/save")
    async def test_save(data: dict):
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = add_user(name, email, password, phone, now)
        return wrap_response(user)

    @app.get("/users/sessions/list")
    async def get_user_sessions_list(user_id: int):
        print(f"invoke >> get_user_sessions_list | user_id {user_id}")
        session_list = get_sessions_by_user_id(user_id)
        print(f"user_id {user_id} session_list {session_list}")
        return wrap_response(session_list)

    @app.post("/chat/change_answer_type")
    async def chat_change_type(data: dict):
        """
        :decs 修改回答类型，推荐或者不推荐
        """
        chat_id = data.get("chat_id")
        answer_type = data.get("answer_type")
        print(f"invoke >> chat_change_type | chat_id {chat_id} | answer_type {answer_type}")
        if answer_type not in [const.answer_type_dislike, const.answer_type_like]:
            return {"message": "invalid chat_type", "data": None}
        update_info = update_chat(chat_id, None, None, None, None, answer_type, None)
        return wrap_response(update_info)
