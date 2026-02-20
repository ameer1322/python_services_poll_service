from typing import Optional

from pydantic import BaseModel

class Question(BaseModel):
    question: str
    answer_a: str
    answer_b: str
    answer_c: str
    answer_d: str