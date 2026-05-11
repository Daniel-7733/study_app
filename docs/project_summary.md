# Project Summary

## What We Want to Build

We want to build a simple desktop study assistant using Python and Tkinter.

The app has four main parts:

1. Timer Page
   - User chooses total study time, for example 2 hours.
   - User chooses break interval, for example every 20 minutes.
   - The app reminds the user to stand up, stretch, or rest for 5 minutes.
   - When the total time is finished, the app says the study session is complete.

2. Notes Page
   - User writes what they learned.
   - Notes are saved locally.
   - SQLite is a good storage choice for this project.

3. Flashcard Creation Page
   - User creates a flashcard from what they learned.
   - Example:
     - Question: What does malloc return in C?
     - Answer: A pointer to allocated memory.

4. Review Page
   - The app shows flashcards that are due for review.
   - Simple review schedule:
     - 3 days after creation
     - 7 days after creation
     - 30 days after creation

## Beginner-Friendly Architecture

The app should follow this simple flow:

UI -> Services -> Database

- UI files handle Tkinter windows and buttons.
- Service files handle logic.
- Database files handle SQLite.
- Model files describe the main objects in the app.

## Folder Structure

study_timer_tkinter/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── timer_page.py
│   │   ├── notes_page.py
│   │   ├── flashcard_page.py
│   │   └── review_page.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── timer_service.py
│   │   ├── notes_service.py
│   │   ├── flashcard_service.py
│   │   └── review_service.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── note.py
│   │   ├── flashcard.py
│   │   └── study_session.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── dates.py
│       ├── helpers.py
│       └── constants.py
│
├── data/
│   └── .gitkeep
│
├── assets/
│   └── icons/
│
└── docs/
    ├── project_summary.md
    └── learning_plan.md
