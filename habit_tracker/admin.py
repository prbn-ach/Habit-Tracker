from django.contrib import admin
from habit_tracker.models import Habit, HabitHistory

admin.site.register(Habit)
admin.site.register(HabitHistory)

# Register your models here.
