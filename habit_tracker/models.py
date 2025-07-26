from django.db import models
from django.utils import timezone

class Habit(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def current_status(self):
        latest = self.history.order_by('-timestamp').first()
        return latest.status if latest else None
    
    def is_completed_today(self):
        today = timezone.now().date()
        latest = self.history.order_by('-timestamp').first()
        return latest and latest.status and latest.timestamp.date() == today

    def current_streak(self):
        from datetime import timedelta
        today = timezone.now().date()
        streak = 0
        day = today
        histories = self.history.filter(status=True).order_by('-timestamp')
        history_dates = set(h.timestamp.date() for h in histories)
        while day in history_dates:
            streak += 1
            day -= timedelta(days=1)
        return streak

    def longest_streak(self):
        from datetime import timedelta
        histories = self.history.filter(status=True).order_by('timestamp')
        if not histories:
            return 0
        streak = 0
        max_streak = 0
        prev_date = None
        for h in histories:
            d = h.timestamp.date()
            if prev_date is None or (d - prev_date).days == 1:
                streak += 1
            else:
                streak = 1
            max_streak = max(max_streak, streak)
            prev_date = d
        return max_streak

class HabitHistory(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='history')
    status = models.BooleanField()  # ✅ True = Completed, False = Not completed
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{'✓' if self.status else '✗'} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


