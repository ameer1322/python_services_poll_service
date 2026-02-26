from typing import List,Optional

from fastapi import APIRouter, HTTPException
from starlette import status

from model.answer_model import Answer
from model.question_model import Question
from service import question_service

router = APIRouter(
    prefix="/question",
    tags=["question"],
)

@router.get("/",status_code = status.HTTP_200_OK)
async def get_questions():
    try:
        return await question_service.get_questions()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@router.post("/", status_code=status.HTTP_200_OK)
async def create_question(question: Question)->int:
    try:
        return await question_service.create_question(question)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_question_by_id/{question_id}", status_code=status.HTTP_200_OK)
async def get_question_by_id(question_id: int)->Optional[Question]:
    try:
        return await question_service.get_question_by_id(question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@router.delete("/delete_question/{question_id}", status_code=status.HTTP_200_OK)
async def delete_question(question_id: int)->Optional[Question]:
    try:
        return await question_service.delete_question(question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_questions_by_users/{user_id}", status_code=status.HTTP_200_OK)
async def get_questions_by_user(user_id: int)->List[Question]:
    try:
        return await question_service.get_questions_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@router.get("/get_question_users_count/{user_id}", status_code=status.HTTP_200_OK)
async def get_question_users_count(user_id: int)->int:
    try:
        return await question_service.get_question_users_count(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

