from pydantic import BaseModel


class BaseRequest(BaseModel):
    """
    Базовая модель на запросы
    """
    pass


class QuestionsRequest(BaseRequest):
    """
    Ответ пользователю на получение уникального вопроса
    """
    id: int
