from datetime import datetime
from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    user_id: int
    title: str
    message: str


class FeedbackResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    created_at: datetime

    class Config:
        orm_mode = True

