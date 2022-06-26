from fastapi import FastAPI, HTTPException, status
from trying_fast_api.data import chats

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/users/{user}/chats")
async def get_user_chats(user: int):
    return [
        {
            "id": chat_id,
            "created_at": chat["created_at"],
            "last_message": (
                chat.get("messages", [])[-1]["text"]
                if len(chat.get("messages",[])) > 0
                else None
            )
        }
        for chat_id, chat in chats.items()
        if chat["seller_id"] == user or chat["buyer_id"] == user
    ]

@app.get("/chats/{chat}/messages")
async def get_chat_messages(chat: str):
    if chat not in chats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return [
        message["text"]
        for message in chats[chat].get("messages", [])
    ]
