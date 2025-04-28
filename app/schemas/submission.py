from pydantic import BaseModel

from datetime import datetime

class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    game_id: int
    question_id: int
    option_id: int
    is_correct:bool
    create_at: datetime


class SubmissionCreate(BaseModel):
    game_id: int
    question_id: int
    option_id: int


