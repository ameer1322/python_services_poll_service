from typing import List,Optional

from fastapi import APIRouter, HTTPException
from starlette import status

from model.answer_model import Answer
from service import answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"],
)

@router.post("/answer_question", status_code=status.HTTP_201_CREATED)
async def answer_question(question_id: int, answer_id: int, user_id:int)->Optional[int]:
    try:
        return await answer_service.answer_question(question_id, answer_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.put("/update_answer", status_code=status.HTTP_200_OK)
async def update_answer(question_id: int, answer_id: int, user_id:int)->Optional[int]:
    try:
        return await answer_service.update_answer(question_id, answer_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/delete_user_answers", status_code=status.HTTP_200_OK)
async def delete_user_answers(user_id: int)->Optional[int]:
    try:
        return await answer_service.delete_answers_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_answers_by_user", status_code=status.HTTP_200_OK)
async def get_answers_by_user(user_id: int)->List[Answer]:
    try:
        return await answer_service.get_answers_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_question_users_answers", status_code=status.HTTP_201_CREATED)
async def get_question_users_answers(user_id: int)->List:
    try:
        return await answer_service.get_question_users_answers(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_users_answers", status_code=status.HTTP_200_OK)
async def get_users_answers(user_id: int)->List[Answer]:
    try:
        return await answer_service.get_users_answers(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_users_answers_count", status_code=status.HTTP_200_OK)
async def get_users_answers_count(user_id: int)->int:
    try:
        return await answer_service.get_users_answers_count(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_all_questions_answers", status_code=status.HTTP_200_OK)
async def get_all_questions_answers(user_id: int)->List:
    try:
        return await answer_service.get_all_questions_answers()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/check_user_answered/{user_id}/{question_id}", status_code=status.HTTP_200_OK)
async def check_user_answered(user_id:int, question_id:int)->bool:
    try:
        return await answer_service.check_user_answered(user_id,question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

