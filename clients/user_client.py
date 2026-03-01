from model.answer_model import Answer

import httpx

USER_SERVICE_URL = "http://localhost:8000"

async def check_user_registered(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{USER_SERVICE_URL}/user/is_registered/{user_id}"
        )
        response.raise_for_status()
        return response.json()