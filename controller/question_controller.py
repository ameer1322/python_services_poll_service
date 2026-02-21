from typing import List,Optional

from fastapi import APIRouter, HTTPException
from starlette import status

from model.answer_model import Answer
from model.question_model import Question
from service import question_service

router = APIRouter(
    prefix="/poll",
    tags=["poll"],
)

@router.post("/", status_code=status.HTTP_200_OK)
async def create_question(question: Question)->int:
    return await question_service.create_question(question)

@router.get("/get_question_by_id/{question_id}", status_code=status.HTTP_200_OK)
async def get_question_by_id(question_id: int)->Optional[Question]:
    return await question_service.get_question_by_id(question_id)

@router.post("/answer_question", status_code=status.HTTP_201_CREATED)
async def answer_question(question_id: int, answer_id: int, user_id:int)->Optional[int]:
    return await question_service.answer_question(question_id, answer_id, user_id)

@router.put("/update_answer", status_code=status.HTTP_200_OK)
async def update_answer(question_id: int, answer_id: int, user_id:int)->Optional[int]:
    return await question_service.update_answer(question_id, answer_id, user_id)

@router.delete("/delete_question/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(question_id: int)->Optional[Question]:
    return await question_service.delete_question(question_id)

@router.delete("/delete_user_answers", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_answers(user_id: int)->Optional[int]:
    return await question_service.delete_answers_by_user(user_id)

@router.get("/get_answers_by_user", status_code=status.HTTP_200_OK)
async def get_answers_by_user(user_id: int)->List[Answer]:
    return await question_service.get_answers_by_user(user_id)

@router.get("/get_questions_by_users", status_code=status.HTTP_200_OK)
async def get_questions_by_user(user_id: int)->List[Question]:
    return await question_service.get_questions_by_user(user_id)

@router.get("/get_question_users_answers", status_code=status.HTTP_201_CREATED)
async def get_question_users_answers(user_id: int)->List:
    return await question_service.get_question_users_answers(user_id)

@router.get("/get_question_users_count", status_code=status.HTTP_200_OK)
async def get_question_users_count(user_id: int)->int:
    return await question_service.get_question_users_count(user_id)

@router.get("/get_users_answers", status_code=status.HTTP_200_OK)
async def get_users_answers(user_id: int)->List[Answer]:
    return await question_service.get_users_answers(user_id)

@router.get("/get_users_answers_count", status_code=status.HTTP_200_OK)
async def get_users_answers_count(user_id: int)->int:
    return await question_service.get_users_answers_count(user_id)

@router.get("/get_all_questions_answers", status_code=status.HTTP_200_OK)
async def get_all_questions_answers(user_id: int)->List:
    return await question_service.get_all_questions_answers()

