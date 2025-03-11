from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.login import create_login_router
from application.chat import create_chat_router
from conf import sgrid_config

app = FastAPI()
# 添加跨域支持
origins = sgrid_config.get("cors_origins")

print(f"添加跨域支持 origins {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_login_router(app)
create_chat_router(app)
