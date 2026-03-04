from pydantic import BaseModel

class QuestionAnswerCount(BaseModel):
    question_id : int
    answer_a : int
    answer_b : int
    answer_c : int
    answer_d : int
