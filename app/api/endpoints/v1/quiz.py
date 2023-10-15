from fastapi import APIRouter
from app.api.services.services import get_lastest_question

router = APIRouter()


@router.post("/api/v1/get_unique_question")
async def questions_num(questions_num: int):
    """
    Возвращет пользователю текст последнего сохраненного вопроса
    или "", если таковой отсутствует.
    """
    return await get_lastest_question(questions_num)