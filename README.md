# Study Web App

A Flask-based study companion for focused learning sessions.

## Features
- Study timer with break reminders
- Notes page for saving what you learned
- Flashcard creation
- Review page for cards due today
- SQLite database for local storage

## Tech Stack
- Python
- Flask
- SQLite
- HTML / CSS / JavaScript

## Project Structure
```text
study_web_app/
├── run.py
├── requirements.txt
├── .gitignore
├── README.md
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   ├── services/
│   ├── database/
│   ├── templates/
│   ├── static/
│   └── utils/
└── data/
```

## How to Run
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate it:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python run.py
   ```
5. Open the local address shown by Flask in your browser.

## Current Routes
- `/` Home page
- `/timer` Timer page
- `/notes` Notes page
- `/flashcards` Flashcard creation page
- `/review` Review page

## Future Ideas
- Edit and delete notes
- Mark flashcards as reviewed
- Session history page
- Authentication
- Better spaced repetition logic
