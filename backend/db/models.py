from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from db.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    profile = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    role = Column(String(20))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)