from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from application.login import create_login_router
from application.chat import create_chat_router
from conf import sgrid_application
from utils import wrap_response

app = FastAPI()


#
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=wrap_response(data=None, message=f"请求异常 {str(exc)}", code=-1)
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=wrap_response(data=None, message=f"服务器内部错误 {str(exc)}", code=-1)
    )


# 添加跨域支持
origins = sgrid_application.get("cors_origins")

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
