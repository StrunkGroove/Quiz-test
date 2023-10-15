from .database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, BigInteger, DateTime


class Questions(Base):
    """
    Модель для уникальных вопроов
    """
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    id_question = Column(Integer, unique=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime())
    timestamp = Column(
        BigInteger,
        server_default=func.extract('epoch', func.now()).cast(BigInteger)
    )
