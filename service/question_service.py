from typing import Optional, List

from model.answer_model import Answer
from model.question_model import Question

from repository import question_repository

async def create_question(question: Question) -> int:
    return await question_repository.create_question(question)

async def get_question_by_id(question_id : int)->Optional[Question]:
    return await question_repository.get_question_by_id(question_id)

async def answer_question(question_id: int, answer_id: int, user_id: int)->Optional[int]:
    return await question_repository.answer_question(question_id, answer_id, user_id)

async def update_answer(question_id: int, answer_id : int, user_id: int)->Optional[int]:
    return await question_repository.update_answer(question_id, answer_id, user_id)

async def delete_question(question_id: int)->Optional[Question]:
    return await question_repository.delete_question(question_id)

async def delete_answers_by_user(user_id: int)->Optional[int]:
    return await question_repository.delete_answers_by_user(user_id)

async def get_answers_by_user(user_id: int)->List[Answer]:
    return await question_repository.get_answers_by_user(user_id)

async def get_questions_by_user(user_id: int)->List[Question]:
    return await question_repository.get_questions_by_user(user_id)

async def get_question_users_answers(question_id: int)->List:
    return await question_repository.get_question_users_answers(question_id)

async def get_question_users_count(question_id: int)->int:
    return await question_repository.get_question_users_count(question_id)

async def get_users_answers(user_id: int)->List[Answer]:
    return await question_repository.get_users_answers(user_id)

async def get_users_answers_count(user_id: int)->int:
    return await question_repository.get_users_answers_count(user_id)

async def get_all_questions_answers()->List:
    return await question_repository.get_all_questions_answers()