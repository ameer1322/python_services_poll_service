from typing import List, Optional, Dict

import traceback

from fastapi import APIRouter, HTTPException
from starlette import status


from model.answer_model import Answer
from model.answer_request_model import AnswerRequest
from service import answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def answer_question(request : AnswerRequest)->Optional[int]:
    try:
        response = await answer_service.answer_question(request.question_id, request.answer_id, request.user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.put("/", status_code=status.HTTP_200_OK)
async def update_answer(request: AnswerRequest)->Optional[int]:
    try:
        return await answer_service.update_answer(request.question_id, request.answer_id, request.user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/delete_user_answers/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user_answers(user_id: int)->List:
    try:
        return await answer_service.delete_answers_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/delete_answer/user/{user_id}/question/{question_id}", status_code=status.HTTP_200_OK)
async def delete_answer(user_id, question_id):
    try:
        return await answer_service.delete_answer(user_id,question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_answers_by_user/{user_id}", status_code=status.HTTP_200_OK)
async def get_answers_by_user(user_id: int)->List[Answer]:
    try:
        return await answer_service.get_answers_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


@router.get("/get_user_answers/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_answers(user_id: int)->List[Answer]:
    try:
        return await answer_service.get_user_answers(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

##get how many questions this user answered
@router.get("/get_user_answers_count/{user_id}", status_code=status.HTTP_200_OK)
async def get_users_answers_count(user_id: int)->int:
    try:
        return await answer_service.get_users_answers_count(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/get_all_questions_answers", status_code=status.HTTP_200_OK)
async def get_all_questions_answers()->Optional[List[dict]]:
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

@router.get("/get_question_answered_count/{user_id}", status_code=status.HTTP_200_OK)
async def get_question_answered_count(question_id: int)->int:
    try:
        return await answer_service.get_question_answered_count(question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

##return how many users choose each of the question options
@router.get("questions_answers_count", status_code=status.HTTP_200_OK)
async def get_questions_answers_count(question_id: int)->List[Dict]:
    try:
        return await answer_service.get_questions_answers_count(question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
