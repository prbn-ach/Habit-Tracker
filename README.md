# Habit Tracker

A minimal habit tracker built with Django. It features:

- A calendar view to mark habit completion with checkmarks  
- Tracks **current** and **longest** habit streaks

## Setup

### 1. Clone the repository


git clone https://github.com/prbn-ach/Habit-Tracker.git
cd Habit-Tracker

### 2. Create and activate a virtual environment

python -m venv venv  
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Apply database migrations

python manage.py migrate

### 5. Run the development server

python manage.py runserver

### 6. Open in your browser

Visit: http://127.0.0.1:8000/
