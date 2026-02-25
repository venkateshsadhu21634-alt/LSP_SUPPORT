from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.chat import ChatMessage
from app.schemas.chat_schema import ChatCreate, ChatResponse
from typing import List


router = APIRouter(
    prefix="/api/v1/support/chat",
    tags=["Chat"]
)


@router.post("/message", response_model=ChatResponse, status_code=201)
def send_chat(data: ChatCreate, db: Session = Depends(get_db)):
    chat = ChatMessage(
        user_id=data.user_id,
        message=data.message,
        sender="user"   # default sender
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


@router.get("/history", response_model=List[ChatResponse])
def chat_history(user_id: int, db: Session = Depends(get_db)):
    """
    Example:
    /api/v1/support/chat/history?user_id=1
    """

    return db.query(ChatMessage).filter(
        ChatMessage.user_id == user_id
    ).all()