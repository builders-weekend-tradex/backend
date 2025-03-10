from fastapi import APIRouter
from pydantic import BaseModel
from utils.fundamental_analysis.lexi import lexi_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/analysis/lexi/")
def chat_with_lexi(request: ChatRequest):
    response = lexi_chat(request.message)
    return {"response": response}