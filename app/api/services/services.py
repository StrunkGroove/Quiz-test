from typing import List
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.models import Questions
from app.database.database import engine
from app.schemas.responses import ParsResponse, QuestionResponse
from app.api.parsing.parsing import pars_questions


async def get_lastest_question(questions_num: int) -> QuestionResponse:
    """
    Запрос вопросов по указанному количеству пользователя.
    Проверка на уникальность вопросов (новый запрос если есть неуникальные вопросы).
    Сохранение уникальных вопросов в БД.
    """

    def check_existing_ids(session: Session, all_ids: List[int]) -> List[int]:
        """
        Проверяем id на уникальность
        """
        query = select(Questions.id_question) \
            .filter(Questions.id_question.in_(all_ids))
        result = session.execute(query)
        existing_ids = [row[0] for row in result.fetchall()]
        return existing_ids

    def save_questions(session: Session, questions: List[ParsResponse]) -> None:
        """
        Cохраняем уникальные вопросы
        """
        question_objects = [
            Questions(
                id_question=question.id,
                question=question.question,
                answer=question.answer,
                created_at=question.created_at,
            )
            for question in questions
        ]
        
        session.add_all(question_objects)
        session.commit()

    def get_last_save_questions(session: Session) -> List[str]:
        """
        Получаем последние сохраненные вопросы
        """
        max_timestamp_subquery = (
            select([func.max(Questions.timestamp)])
            .as_scalar()
            .label("max_timestamp")
        )

        questions = (
            session.query(Questions.question)
            .filter(Questions.timestamp == max_timestamp_subquery)
            .all()
        )
        return [q[0] for q in questions] if questions else ['']

    max_attentional = 10
    attentional = 0

    with Session(engine) as session:
        while(attentional<=max_attentional):

            data = await pars_questions(questions_num)

            if isinstance(data, HTTPException):
                continue
            
            all_ids = [item.id for item in data]
            existing_ids = check_existing_ids(session, all_ids)
            unique_questions = [item for item in data if item.id not in existing_ids]

            if len(unique_questions) == 0: 
                continue

            questions = get_last_save_questions(session)

            save_questions(session, unique_questions)
            
            return [QuestionResponse(question=q) for q in questions]
    return HTTPException(status_code=404, detail="Question not found")