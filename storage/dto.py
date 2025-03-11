from typing import Union

from pydantic import BaseModel, validator


class ChatDTO(BaseModel):
    chat_msg: str
    session_id: int
    user_id: int
    chat_type: Union[int, None]
    prompts: Union[list, None]
    history: Union[list, None]

    @validator('chat_msg', pre=True)
    def chat_msg_must_not_be_empty(cls, value):
        if value.strip() == '':
            raise ValueError('chat_msg cannot be an empty string')
        return value


class SessionDTO(BaseModel):
    name: str
    user_id: int

    @validator('name', pre=True)
    def name_must_not_be_empty(cls, value):
        if value.strip() == '':
            raise ValueError('name cannot be an empty string')
        return value


class PromptDTO(BaseModel):
    name: str
    user_id: int

    @validator('name', pre=True)
    def name_must_not_be_empty(cls, value):
        if value.strip() == '':
            raise ValueError('name cannot be an empty string')
        return value


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

    @validator('email', pre=True)
    def email_must_not_be_empty(cls, value):
        if value.strip() == '':
            raise ValueError('email cannot be an empty string')
        return value

    @validator('password', pre=True)
    def password_must_not_be_empty(cls, value):
        if value.strip() == '':
            raise ValueError('password cannot be an empty string')
        return value
