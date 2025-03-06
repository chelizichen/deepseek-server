from fastapi import FastAPI

from application.login import create_login_router
from application.chat import create_chat_router

app = FastAPI()

create_login_router(app)
create_chat_router(app)
