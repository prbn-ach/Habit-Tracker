🗓️ Habit Tracker

A minimal habit tracker built with Django. It features:

  A calendar view to mark habit completion with checkmarks ✅

  Tracks current and longest streaks

Setup
git clone https://github.com/prbn-ach/Habit-Tracker.git
cd Habit-Tracker

Create a virtual environment
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Go to 
http://127.0.0.1:8000/
