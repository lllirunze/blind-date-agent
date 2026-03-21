from pydantic import BaseModel

class ChatRequest(BaseModel):
    conversation_id: int
    message: str

class CreateConversationRequest(BaseModel):
    name: str
    profile: str