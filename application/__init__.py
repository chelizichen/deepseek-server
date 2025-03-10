from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.login import create_login_router
from application.chat import create_chat_router

app = FastAPI()
# 添加跨域支持
origins = [
    "http://127.0.0.1:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_login_router(app)
create_chat_router(app)
