from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    """
    Базовая модель на ответы
    """
    model_config = ConfigDict(from_attributes=True)


class QuestionResponse(BaseModel):
    """
    Для ответа на запрос пользователя об уникальных вопросах 
    """
    question: str


class ParsResponse(BaseResponse):
    """
    Принимаем вопросы от парсера
    """
    id: int
    question: str
    answer: str
    created_at: datetime
