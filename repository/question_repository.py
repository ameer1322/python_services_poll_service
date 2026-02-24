from typing import Optional, List

import json
from repository.database import database
from model.question_model import Question
from model.answer_model import Answer

async def get_questions()-> Optional[List[Question]]:
    query = """
            SELECT * FROM poll_questions    
    """
    return await database.fetch_all(query)

async def create_question(question_data: Question) -> int:
    query = """
            INSERT INTO poll_questions (question, answer_a, answer_b, answer_c,answer_d)
            VALUES (:question, :answer_a, :answer_b, :answer_c, :answer_d)
    """

    values ={
        'question': question_data.question,
        'answer_a': question_data.answer_a,
        'answer_b': question_data.answer_b,
        'answer_c': question_data.answer_c,
        'answer_d': question_data.answer_d
    }

    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def get_question_by_id(question_id: int) -> Optional[Question]:
    query = """
        SELECT * FROM poll_questions WHERE id = :question_id
    """

    values = {
        'question_id': question_id
    }

    return await database.fetch_one(query, values)

async def delete_question (question_id: int) -> Optional[Question]:
    query = """
    DELETE FROM poll_questions WHERE id = :question_id
    """
    values = {
        'question_id': question_id
    }
    async with database.transaction():
        deleted_question = await database.fetch_one("SELECT * FROM poll_questions WHERE id = :question_id", values)
        await database.execute(query, values)
    return deleted_question


async def get_questions_by_user (user_id: int) -> List:
    query = """
    SELECT * FROM poll_questions 
    JOIN poll_answers ON poll_questions.id = poll_answers.question_id
    WHERE poll_answers.user_id = :user_id
    """
    values = {
        'user_id': user_id
    }
    return await database.fetch_all(query, values=values)

async def get_question_users_count(question_id: int) -> int:
    query = """
    SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id
    """
    values = {
        'question_id': question_id
    }
    return await database.fetch_one(query, values)



