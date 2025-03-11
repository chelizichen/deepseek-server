from typing import Union

from pydantic import BaseModel


class ChatDTO(BaseModel):
    chat_msg: str
    session_id: int
    user_id: int
    chat_type: Union[int, None]
    prompts: Union[list, None]
    history: Union[list, None]


class SessionDTO(BaseModel):
    name: str
    user_id: int


class PromptDTO(BaseModel):
    name: str
    user_id: int


class ChatPromptsDTO(BaseModel):
    session_id: int
    user_id: int
    prompt_ids: list


class UserDTO(BaseModel):
    name: str
    email: str
    password: str
    phone: str


class ChangeAnswerTypeDTO(BaseModel):
    chat_id: int
    answer_type: int


class LoginDTO(BaseModel):
    email: str
    password: str
