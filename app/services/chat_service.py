from sqlalchemy.orm import Session
from app.models.chat import Chat
from app.schemas.chat_schema import ChatCreate
from app.repositories.chat_repository import ChatRepository


class ChatService:

    def __init__(self):
        self.repo = ChatRepository()

    def send_message(self, db: Session, data: ChatCreate):

        chat = Chat(
            user_id=data.user_id,
            message=data.message
        )

        return self.repo.create_message(db, chat)

    def get_history(self, db: Session, user_id: int):
        return self.repo.get_chat_history(db, user_id)