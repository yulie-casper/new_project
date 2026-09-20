# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: StudyMap
def demo():
    """Демонстрация основного сценария: добавление тем, прогресс и проверка знаний."""
    plan = StudyPlan("Python-курс")
    plan.add_topic("Введение в Python", "Базовые типы данных", 5)
    plan.add_topic("Структуры данных", "Списки и словари", 8)
    plan.add_topic("Функции", "Область видимости и замыкания", 6)
    plan.add_topic("ООП", "Классы и наследование", 10)

    print(f"Всего тем: {plan.total_topics}")
    print(f"Всего контрольных: {plan.total_quizzes}")

    progress = plan.get_progress()
    print(f"Прогресс: {progress['completed']} / {progress['total']} тем пройдено")

    if progress['completed'] >= progress['total']:
        print("🎉 Поздравляю! Вы прошли весь курс!")
    else:
        print(f"Осталось пройти {progress['total'] - progress['completed']} тем")

    plan.check_topic("Введение в Python")
    print(f"\nРезультат контрольной по 'Введение в Python': {plan.check_topic('Введение в Python')}")
