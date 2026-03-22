from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal, Base, engine
from schemas.chat_schema import ChatRequest, CreateConversationRequest
from repository.chat_repo import create_conversation, list_conversations, get_conversation
from service.chat_service import process_chat

app = FastAPI()

# 自动建表
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/conversation")
def create_conv(req: CreateConversationRequest, db: Session = Depends(get_db)):
    return create_conversation(db, req.name, req.profile)


@app.get("/conversation")
def list_conv(db: Session = Depends(get_db)):
    return list_conversations(db)


@app.post("/chat")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    conv = get_conversation(db, req.conversation_id)

    if not conv:
        return {"error": "conversation not found"}

    result = process_chat(db, conv, req.message)

    return result