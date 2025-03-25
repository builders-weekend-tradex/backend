from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.lexi import lexi_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/analysis/lexi/")
async def chat_with_lexi(request: Request, chat_request: ChatRequest):
    response = lexi_chat(chat_request.message)
    return {"response": response}