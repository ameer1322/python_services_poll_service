from typing import Optional

from pydantic import BaseModel

class Answer(BaseModel):
    question_id: int
    answer_id: int