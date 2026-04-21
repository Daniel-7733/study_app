from datetime import datetime
from pathlib import Path

from app.database.connection import get_connection


def save_note(db_path: str | Path, title: str, content: str) -> None:
    """Save a note to the database."""
    title = title.strip()
    content = content.strip()

    if not title or not content:
        raise ValueError('Title and content are required.')

    connection = get_connection(db_path)
    try:
        connection.execute(
            'INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)',
            (title, content, datetime.now().isoformat(timespec='seconds')),
        )
        connection.commit()
    finally:
        connection.close()


def get_all_notes(db_path: str | Path) -> list[dict]:
    """Return all notes ordered from newest to oldest."""
    connection = get_connection(db_path)
    try:
        rows = connection.execute(
            'SELECT id, title, content, created_at FROM notes ORDER BY id DESC'
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()
