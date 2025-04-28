from pydantic import BaseModel

from datetime import  datetime


class OptionResponse(BaseModel):
    id: int
    question_id: str
    is_correct: bool
    create_at: datetime

class OptionCreate(BaseModel):
    title: str
    question_id: int
    question_id: int
    is_correct: bool


class OptionUpdate(BaseModel):
    title: str | None = None
    is_correct: bool | None = None



