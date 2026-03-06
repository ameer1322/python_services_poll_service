from typing import Optional, List

from model.user_model import User
from model.answer_model import Answer
from model.question_model import Question

from clients import user_client

from repository import question_repository

async def create_question(question: Question) -> int:
    return await question_repository.create_question(question)

async def get_question_by_id(question_id : int)->Optional[Question]:
    question = await question_repository.get_question_by_id(question_id)
    if question:
        return question
    raise ValueError("Question not found")

async def delete_question(question_id: int)->Optional[Question]:
    question = await question_repository.get_question_by_id(question_id)
    if question:
        return await question_repository.delete_question(question_id)
    raise ValueError("Question not found")

async def get_questions_by_user(user_id: int)->List[Question]:
    user_response = await user_client.get_user(user_id)
    if user_response["status_code"] == 404:
        raise ValueError("User not found")
    return await question_repository.get_questions_by_user(user_id)





async def get_questions()-> Optional[List[Question]]:
    return await question_repository.get_questions()