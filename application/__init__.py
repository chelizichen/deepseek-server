from service.service import ai_programmer as ai_programmer_service
from fastapi import FastAPI
from storage.storage import add_user

app = FastAPI()


@app.get("/greet")
async def root():
    return {"message": "Hello World"}


@app.get("/chat/ai_programmer")
async def ai_programmer(chat_msg: str):
    return ai_programmer_service(chat_msg)


@app.get("/test/save")
async def test_save():
    user = add_user("John Doe11", "john@example.com")
    return user
