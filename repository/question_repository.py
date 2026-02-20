from typing import Optional, List

import json
from repository.database import database
from model.question_model import Question
from model.answer_model import Answer

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


async def answer_question (question_id: int, answer_id: int, user_id: int) -> Optional[int]:
    if answer_id > 4 or answer_id < 0:
        raise ValueError('answer_id must be between 1 and 4')
    query = """
    INSERT into poll_answers (question_id, answer_id, user_id)
    VALUES (:question_id, :answer_id, :user_id)
    """
    values = {
        'question_id': question_id,
        'answer_id': answer_id,
        'user_id': user_id
    }
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def update_answer (question_id: int, answer_id: int, user_id: int) -> Optional[int]:
    if answer_id > 4 or answer_id < 0:
        raise ValueError('answer_id must be between 1 and 4')
    query = """
    UPDATE poll_answers 
    SET answer_id = :answer_id
    WHERE user_id = :user_id AND question_id = :question_id
    """
    values = {
        'answer_id': answer_id,
        'question_id': question_id,
        'user_id': user_id
    }
    async with database.transaction():
        await database.execute(query, values)

    return question_id


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


async def delete_answers_by_user (user_id: int) -> Optional[List[Answer]]:
    query = """
    DELETE FROM poll_answers WHERE user_id = :user_id
    """
    values = {
        'user_id': user_id
    }
    async with database.transaction():
        deleted_answers = await database.fetch_all("SELECT * FROM poll_answers WHERE user_id = :user_id", values)
        await database.execute(query, values)
    return deleted_answers

async def get_answers_by_user (user_id: int) -> List[Answer]:
    query = """
    SELECT * FROM poll_answers WHERE user_id = :user_id
    """
    values = {
        'user_id': user_id
    }
    return await database.fetch_all(query, values=values)


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

async def get_question_users_answers(question_id: int) -> List:
    question = await get_question_by_id(question_id)
    values = {"question_id": question_id}
    answer_a = await database.fetch_one("SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id AND answer_id = 1", values)
    answer_b = await database.fetch_one("SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id AND answer_id = 2", values)
    answer_c = await database.fetch_one("SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id AND answer_id = 3", values)
    answer_d = await database.fetch_one("SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id AND answer_id = 4", values)
    return [question, answer_a[0], answer_b[0], answer_c[0], answer_d[0]]

async def get_question_users_count(question_id: int) -> int:
    query = """
    SELECT COUNT(answer_id) FROM poll_answers WHERE question_id = :question_id
    """
    values = {
        'question_id': question_id
    }
    return await database.fetch_one(query, values)

async def get_users_answers(user_id: int) -> List:
    query = """
    SELECT * FROM poll_answers WHERE user_id = :user_id
    """
    values = {
        'user_id': user_id
    }
    return await database.fetch_all(query, values=values)

async def get_users_answers_count(user_id: int) -> int:
    query = """
    SELECT COUNT(answer_id) FROM poll_answers WHERE user_id = :user_id
    """
    values = {
        'user_id': user_id
    }
    return await database.fetch_one(query, values)


async def get_all_questions_answers() -> List:
    query = """
    SELECT poll_questions.id, poll_questions.question, poll_questions.answer_a, poll_questions.answer_b, poll_questions.answer_c, poll_questions.answer_d, poll_answers.answer_id, COUNT(*) as count
    FROM poll_questions 
    JOIN poll_answers ON poll_questions.id = poll_answers.question_id
    GROUP BY poll_questions.id, poll_answers.answer_id
    """
    return await database.fetch_all(query)
