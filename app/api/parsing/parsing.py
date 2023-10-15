import httpx

from typing import List
from pydantic import ValidationError
from fastapi import HTTPException

from app.schemas.responses import ParsResponse


async def pars_questions(num: int) -> List[ParsResponse]:
    """
    Парсинг определенного количества вопросов по ссылке
    """
    url = f"https://jservice.io/api/random?count={num}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()

        try:
            return [ParsResponse(**item) for item in data]
        except ValidationError as e:
            return None
    else:
        return None
