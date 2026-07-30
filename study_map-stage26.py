# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: StudyMap
def demo_commands():
    print("=" * 50)
    print("DEMO: Быстрое ручное тестирование StudyMap")
    print("=" * 50)

    # Команда 1: показать все темы
    print("\n--- Тема 1 ---")
    show_topic(1, topics[0], materials[0])

    # Команда 2: показать материалы по теме
    print("\n--- Материалы к теме 1 ---")
    show_materials(topics[0], materials[0])

    # Команда 3: добавить прогресс
    print("\n--- Прогресс ---")
    add_progress(1, "Освоена", topics[0])

    # Команда 4: проверка контрольной точки
    print("\n--- Контрольная точка ---")
    check_checkpoint(topics[0], materials[0])

    # Команда 5: общий прогресс
    print("\n--- Общий прогресс ---")
    show_overall_progress()

    print("\nВсе демо-команды успешно выполнены!")
