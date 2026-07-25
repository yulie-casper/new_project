# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: StudyMap
def check_overdue_reminders(self):
    """Проверяет просроченные напоминания и выводит предупреждения."""
    for topic in self.topics:
        if topic.reminder_date and topic.reminder_date < datetime.now().date():
            print(f"⚠️  Напоминание о теме '{topic.name}' истекло {datetime.now() - topic.reminder_date}.")

self.check_overdue_reminders()
