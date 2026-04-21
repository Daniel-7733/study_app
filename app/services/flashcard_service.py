from datetime import date, datetime, timedelta
from pathlib import Path

from app.database.connection import get_connection


REVIEW_STAGES = {
    0: 3,
    1: 7,
    2: 30,
}


def calculate_next_review(stage: int) -> str:
    """Return the next review date based on the current stage."""
    days = REVIEW_STAGES.get(stage, 30)
    return (date.today() + timedelta(days=days)).isoformat()


def create_flashcard(db_path: str | Path, question: str, answer: str) -> None:
    """Save a new flashcard into the database."""
    question = question.strip()
    answer = answer.strip()

    if not question or not answer:
        raise ValueError('Question and answer are required.')

    connection = get_connection(db_path)
    try:
        connection.execute(
            '''
            INSERT INTO flashcards (question, answer, created_at, review_stage, next_review_date)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                question,
                answer,
                datetime.now().isoformat(timespec='seconds'),
                0,
                calculate_next_review(0),
            ),
        )
        connection.commit()
    finally:
        connection.close()


def get_due_flashcards(db_path: str | Path) -> list[dict]:
    """Return flashcards that are due today or earlier."""
    today = date.today().isoformat()
    connection = get_connection(db_path)
    try:
        rows = connection.execute(
            '''
            SELECT id, question, answer, created_at, review_stage, next_review_date
            FROM flashcards
            WHERE next_review_date <= ?
            ORDER BY next_review_date ASC, id ASC
            ''',
            (today,),
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()
