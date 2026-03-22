from sqlalchemy.orm import Session
from db.models import Message, Conversation


def create_conversation(db: Session, name: str, profile: str):
    conv = Conversation(name=name, profile=profile)
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conv


def get_conversation(db: Session, conversation_id: int):
    return db.query(Conversation).filter_by(id=conversation_id).first()


def list_conversations(db: Session):
    return db.query(Conversation).all()


def save_message(db: Session, conversation_id: int, role: str, content: str):
    msg = Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def get_history(db: Session, conversation_id: int):
    return db.query(Message)\
        .filter_by(conversation_id=conversation_id)\
        .order_by(Message.created_at.asc())\
        .all()