from typing import Optional, List

from model.answer_model import Answer
from model.question_model import Question

from repository import answer_repository
from service import question_service

from clients import user_client

async def answer_question(question_id: int, answer_id: int, user_id: int)->Optional[int]:
    is_registered = await user_client.check_user_registered(user_id)
    if is_registered:
        return await answer_repository.answer_question(question_id, answer_id, user_id)
    raise ValueError ("User needs to be registered")

async def update_answer(question_id: int, answer_id : int, user_id: int)->Optional[int]:
    is_registered = await user_client.check_user_registered(user_id)
    if is_registered:
        return await answer_repository.update_answer(question_id, answer_id, user_id)
    raise ValueError ("User needs to be registered")

async def delete_answers_by_user(user_id: int)->List:
    return await answer_repository.delete_answers_by_user(user_id)

async def delete_answer(user_id: int, question_id: int):
    return await answer_repository.delete_answer(user_id,question_id)

async def get_answers_by_user(user_id: int)->List[Answer]:
    return await answer_repository.get_answers_by_user(user_id)

async def get_question_users_answers(question_id: int)->List:
    return await answer_repository.get_question_users_answers(question_id)

async def get_user_answers(user_id: int)->List[Answer]:
    return await answer_repository.get_user_answers(user_id)

async def get_users_answers_count(user_id: int)->int:
    return await answer_repository.get_users_answers_count(user_id)

async def get_all_questions_answers()->Optional[List[dict]]:
    return await answer_repository.get_all_questions_answers()

async def check_user_answered(user_id: int, question_id:int)->bool:
    question = await question_service.get_question_by_id(question_id)
    if question:
        return await answer_repository.check_user_answered(user_id, question_id)
    raise ValueError ("Question doesn't exist")

async def get_question_answered_count(question_id: int)->int:
    return await answer_repository.get_question_answered_count(question_id)

async def get_questions_answers_count(question_id: int)->List[dict]:
    return await answer_repository.get_questions_answers_count(question_id)