from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="active")

    
    complaints = relationship("Complaint", back_populates="user")
    chat_messages = relationship("ChatMessage", back_populates="user")