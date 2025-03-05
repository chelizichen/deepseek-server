from conf.init import sgrid_config
import uvicorn
from ai.service import ai_programmer as ai_programmer_service
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
async def root():
    return {"message": "Hello World"}


@app.get("/chat/ai_programmer")
async def ai_programmer(chat_msg: str):
    return ai_programmer_service(chat_msg)


def main():
    # 解析命令行参数
    port = sgrid_config.get_port()
    print(f"Sgrid-Python[load port] {port}")
    # 启动 uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
