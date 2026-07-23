# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: StudyMap
import datetime
from collections import defaultdict

# Простая система напоминаний для StudyMap
def add_reminder(tasks, reminder_dates):
    """Добавить напоминание о дате выполнения к задаче."""
    task_id = input("Введите ID задачи: ")
    date_str = input("Введите дату (YYYY-MM-DD): ")
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        reminder_dates[task_id] = date_obj
        print(f"Напоминание добавлено к задаче {task_id} на {date_obj}")
    except ValueError:
        print("Неверный формат даты!")

def check_reminders(reminder_dates, current_date=None):
    """Проверить напоминания и показать ближайшие."""
    if current_date is None:
        current_date = datetime.date.today()
    
    upcoming = []
    for task_id, date in reminder_dates.items():
        days_left = (date - current_date).days
        if 0 <= days_left <= 7:
            upcoming.append((task_id, date, days_left))
    
    if upcoming:
        print("Ближайшие напоминания:")
        for task_id, date, days in sorted(upcoming):
            status = "Сегодня!" if days == 0 else f"Через {days} дней"
            print(f"  - Задача {task_id}: {status}")
    else:
        print("Нет предстоящих напоминаний.")

def show_reminders(reminder_dates):
    """Показать все активные напоминания."""
    if not reminder_dates:
        print("Напоминания не добавлены.")
        return
    
    current_date = datetime.date.today()
    print("Активные напоминания:")
    for task_id, date in reminder_dates.items():
        days_left = (date - current_date).days
        if days_left >= 0:
            status = "Выполнено" if days_left < 0 else f"Через {days_left} дней"
            print(f"  - Задача {task_id}: {status}")

# Пример использования
tasks = {"Python Basics": True, "Data Structures": False}
reminder_dates = {}
add_reminder(tasks, reminder_dates)
show_reminders(reminder_dates)
