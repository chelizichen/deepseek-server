from conf.db import Session, Sessions, Users, Chats, Prompts, ChatsPrompts, ChatLock
import application.const as const
from sqlalchemy import text

# 倒序实现方式
# from sqlalchemy import desc
# order_by(desc(Chats.id))

"""
****************************** USER **************************
"""


# 用户相关操作
def add_user(name, email, password, phone, create_time):
    session = Session()
    new_user = Users(name=name, email=email, password=password, phone=phone, create_time=create_time)
    session.add(new_user)
    session.commit()
    user_dict = {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "password": new_user.password,
        "phone": new_user.phone,
        "create_time": new_user.create_time
    }
    session.close()
    return user_dict


def get_user(user_id):
    session = Session()
    user = session.query(Users).filter_by(id=user_id).first()
    session.close()
    return user


def update_user(user_id, name=None, email=None, password=None, phone=None, create_time=None):
    session = Session()
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        if phone:
            user.phone = phone
        if create_time:
            user.create_time = create_time
        session.commit()
    session.close()
    return user


def delete_user(user_id):
    session = Session()
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
    return user


"""
****************************** USER **************************
"""

"""
****************************** CHAT **************************
"""


# 聊天记录相关操作
def add_chat(user_id, question, answer, typ, answer_type, create_time, session_id):
    session = Session()
    new_chat = Chats(user_id=user_id, question=question, answer=answer, type=typ, answer_type=answer_type,
                     create_time=create_time, session_id=session_id)
    session.add(new_chat)
    session.commit()
    chat_dict = {
        "id": new_chat.id,
        "user_id": new_chat.user_id,
        "question": new_chat.question,
        "answer": new_chat.answer,
        "type": new_chat.type,
        "answer_type": new_chat.answer_type,
        "create_time": new_chat.create_time,
        "session_id": new_chat.session_id
    }
    session.close()
    return chat_dict


def get_chat_history_by_session_id(session_id: int) -> list[Chats]:
    session = Session()
    chats = session.query(Chats).order_by(Chats.id).filter(
        Chats.session_id == session_id,
        Chats.answer_type != const.answer_type_dislike,
        Chats.type != const.chat_type_abstract
    ).all()
    session.close()
    return chats


def get_chat_history_inference_by_session_id(session_id: int) -> list[Chats]:
    session = Session()
    chats = session.execute(text(f"""
SELECT c2.*
FROM chats c2
WHERE 
1 = 1
AND c2.id >= IFNULL(
    (SELECT MAX(c.id) FROM chats c WHERE c.session_id = {session_id} AND c.type = {const.chat_type_abstract}),
    0
)
AND c2.session_id = {session_id}
AND c2.answer_type != {const.answer_type_dislike};
        """)).all()
    session.close()
    return chats


def get_prompts_by_session_id(session_id: int):
    session = Session()
    prompts = session.query(ChatsPrompts, Prompts.name).join(
        Prompts, ChatsPrompts.prompt_id == Prompts.id, isouter=True
    ).filter(ChatsPrompts.session_id == session_id).all()
    session.close()
    result = []
    for chat_prompt, prompt_name in prompts:
        chat_prompt_dict = {
            "id": chat_prompt.id,
            "session_id": chat_prompt.session_id,
            "user_id": chat_prompt.user_id,
            "prompt_id": chat_prompt.prompt_id,
            "prompt_name": prompt_name
        }
        result.append(chat_prompt_dict)
    return result


def get_chat(chat_id):
    session = Session()
    chat = session.query(Chats).filter_by(id=chat_id).first()
    session.close()
    return chat


def get_chat_by_session_id(session_id):
    session = Session()
    chats = session.query(Chats).filter_by(session_id=session_id).all()
    session.close()
    return chats


def update_chat(chat_id, user_id=None, question=None, answer=None, chat_type=None, answer_type=None, create_time=None):
    session = Session()
    chat = session.query(Chats).filter_by(id=chat_id).first()
    if chat:
        if user_id:
            chat.user_id = user_id
        if question:
            chat.question = question
        if answer:
            chat.answer = answer
        if chat_type:
            chat.type = chat_type
        if answer_type:
            chat.answer_type = answer_type
        if create_time:
            chat.create_time = create_time
        session.commit()
    session.close()
    return chat


def delete_chat(chat_id):
    session = Session()
    chat = session.query(Chats).filter_by(id=chat_id).first()
    if chat:
        session.delete(chat)
        session.commit()
    session.close()
    return chat


"""
****************************** CHAT **************************
"""
"""
****************************** PROMPT **************************
"""


# 提示词相关操作
def add_prompt(name, use_count, create_user_id, create_time):
    session = Session()
    new_prompt = Prompts(name=name, use_count=use_count, create_user_id=create_user_id, create_time=create_time)
    session.add(new_prompt)
    session.commit()
    prompt_dict = {
        "id": new_prompt.id,
        "name": new_prompt.name,
        "use_count": new_prompt.use_count,
        "create_user_id": new_prompt.create_user_id,
        "create_time": new_prompt.create_time
    }
    session.close()
    return prompt_dict


def get_prompt(prompt_id):
    session = Session()
    prompt = session.query(Prompts).filter_by(id=prompt_id).first()
    session.close()
    return prompt


def update_prompt(prompt_id, name=None, use_count=None, create_user_id=None, create_time=None):
    session = Session()
    prompt = session.query(Prompts).filter_by(id=prompt_id).first()
    if prompt:
        if name:
            prompt.name = name
        if use_count:
            prompt.use_count = use_count
        if create_user_id:
            prompt.create_user_id = create_user_id
        if create_time:
            prompt.create_time = create_time
        session.commit()
    session.close()
    return prompt


def delete_prompt(prompt_id):
    session = Session()
    prompt = session.query(Prompts).filter_by(id=prompt_id).first()
    if prompt:
        session.delete(prompt)
        session.commit()
    session.close()
    return prompt


"""
****************************** PROMPT **************************
"""
"""
****************************** CHAT_PROMPT **************************
"""


# 聊天记录和提示词关联表相关操作
def add_chat_prompt(session_id, user_id, prompt_id):
    session = Session()
    new_chat_prompt = ChatsPrompts(session_id=session_id, user_id=user_id, prompt_id=prompt_id)
    session.add(new_chat_prompt)
    session.commit()
    chat_prompt_dict = {
        "id": new_chat_prompt.id,
        "session_id": new_chat_prompt.session_id,
        "user_id": new_chat_prompt.user_id,
        "prompt_id": new_chat_prompt.prompt_id
    }
    session.close()
    return chat_prompt_dict


def get_chat_prompt(chat_prompt_id):
    session = Session()
    chat_prompt = session.query(ChatsPrompts).filter_by(id=chat_prompt_id).first()
    session.close()
    return chat_prompt


def update_chat_prompt(chat_prompt_id, chat_id=None, user_id=None):
    session = Session()
    chat_prompt = session.query(ChatsPrompts).filter_by(id=chat_prompt_id).first()
    if chat_prompt:
        if chat_id:
            chat_prompt.chat_id = chat_id
        if user_id:
            chat_prompt.user_id = user_id
        session.commit()
    session.close()
    return chat_prompt


def delete_chat_prompt(chat_prompt_id):
    session = Session()
    chat_prompt = session.query(ChatsPrompts).filter_by(id=chat_prompt_id).first()
    if chat_prompt:
        session.delete(chat_prompt)
        session.commit()
    session.close()
    return chat_prompt


"""
****************************** CHAT_PROMPT **************************
"""
"""
****************************** SESSION **************************
"""


# 添加会话记录
def add_session(create_user_id, name, create_time):
    session = Session()
    try:
        new_session = Sessions(
            create_user_id=create_user_id,
            name=name,
            create_time=create_time
        )
        session.add(new_session)
        session.commit()
        session_info = {
            "id": new_session.id,
            "create_user_id": new_session.create_user_id,
            "name": new_session.name,
            "create_time": new_session.create_time
        }
        return session_info
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 获取会话记录
def get_session(session_id):
    session = Session()
    try:
        session_record = session.query(Sessions).filter_by(id=session_id).first()
        return session_record
    except Exception as e:
        raise e
    finally:
        session.close()


def get_sessions_by_user_id(user_id):
    session = Session()
    try:
        session_record = session.query(Sessions).filter_by(create_user_id=user_id).all()
        return session_record
    except Exception as e:
        raise e
    finally:
        session.close()


# 更新会话记录
def update_session(session_id, create_user_id=None, name=None, chat_id=None, create_time=None):
    session = Session()
    try:
        session_record = session.query(Sessions).filter_by(id=session_id).first()
        if session_record:
            if create_user_id:
                session_record.create_user_id = create_user_id
            if name:
                session_record.name = name
            if chat_id:
                session_record.chat_id = chat_id
            if create_time:
                session_record.create_time = create_time
            session.commit()
        return session_record
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 删除会话记录
def delete_session(session_id):
    session = Session()
    try:
        session_record = session.query(Sessions).filter_by(id=session_id).first()
        s_id = 0
        if session_record:
            session_record.status = const.session_delete
            s_id = session_record.id
            session.commit()
        return s_id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


"""
****************************** SESSION **************************
"""

"""
1. create_session
2. create prompts_map with session 
3. chat 
"""

"""
****************************** LOGIN **************************
"""


def user_login(email):
    session = Session()
    user = session.query(Users).filter_by(email=email).first()
    session.close()
    return user


"""
****************************** LOGIN **************************
"""


# 新增 ChatLock 记录
def add_chat_lock(session_id, status):
    session = Session()
    try:
        chat_lock = ChatLock(session_id=session_id, chat_status=status)
        session.add(chat_lock)
        session.commit()
        return chat_lock
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 根据 id 删除 ChatLock 记录
def delete_chat_lock(session_id):
    session = Session()
    try:
        chat_lock = session.query(ChatLock).filter_by(session_id=session_id).first()
        if chat_lock:
            session.delete(chat_lock)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 根据 id 更新 ChatLock 记录
def update_chat_lock(session_id=None, status=None) -> bool:
    session = Session()
    try:
        chat_lock = session.query(ChatLock).filter_by(session_id=session_id).first()
        if status == const.chat_lock & chat_lock.chat_status == const.chat_lock:
            return False
        if chat_lock:
            if session_id is not None:
                chat_lock.session_id = session_id
            if status is not None:
                chat_lock.chat_status = status
            session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 根据 session_id 查询 ChatLock 记录
def get_chat_locks_by_session_id(session_id):
    session = Session()
    try:
        chat_locks = session.query(ChatLock).filter_by(session_id=session_id).all()
        return chat_locks
    except Exception as e:
        raise e
    finally:
        session.close()
