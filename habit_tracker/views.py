from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Habit, HabitHistory
from .forms import HabitForm


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habit_tracker/habit_list.html', {'habits': habits})


def habit_create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/habit_form.html', {'form': form})


def habit_detail(request, habit_id):
    import calendar
    from datetime import date
    habit = get_object_or_404(Habit, id=habit_id)
    history = habit.history.order_by('-timestamp')

    # Calendar logic
    today = timezone.now().date()
    year = today.year
    month = today.month
    cal = calendar.Calendar(calendar.SUNDAY)  # Start week on Sunday
    month_days = cal.itermonthdates(year, month)
    # Build a dict of {date: status}
    day_status = {}
    for h in habit.history.filter(timestamp__year=year, timestamp__month=month):
        d = h.timestamp.date()
        day_status[d] = h.status
    # Build a list of weeks, each week is a list of (date, status)
    month_calendar = []
    week = []
    for day in month_days:
        if day.month != month:
            week.append((day, None))  # Not in this month
        else:
            week.append((day, day_status.get(day)))
        if len(week) == 7:
            month_calendar.append(week)
            week = []
    if week:
        month_calendar.append(week)

    return render(request, 'habit_tracker/habit_detail.html', {
        'habit': habit,
        'history': history,
        'month_calendar': month_calendar,
    })

@require_POST
def habit_mark_complete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    today = timezone.now().date()
    history_today = habit.history.filter(timestamp__date=today).first()
    if history_today:
        history_today.status = True
        history_today.timestamp = timezone.now()  # Optionally update timestamp
        history_today.save()
    else:
        HabitHistory.objects.create(habit=habit, status=True, timestamp=timezone.now())
    return redirect('habit_detail', habit_id=habit.id)

@require_POST
def habit_mark_incomplete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    today = timezone.now().date()
    history_today = habit.history.filter(timestamp__date=today).first()
    if history_today:
        history_today.status = False
        history_today.timestamp = timezone.now()  # Optionally update timestamp
        history_today.save()
    else:
        HabitHistory.objects.create(habit=habit, status=False, timestamp=timezone.now())
    return redirect('habit_detail', habit_id=habit.id)


def habit_edit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_detail', habit_id=habit.id)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit_tracker/habit_form.html', {'form': form, 'habit': habit, 'edit_mode': True})


def habit_delete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit_list')
    return render(request, 'habit_tracker/habit_confirm_delete.html', {'habit': habit})
