# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: StudyMap
def check_and_fix_data():
    """Проверка целостности данных и автоматический ремонт простых проблем."""
    if not all(isinstance(t, dict) for t in themes):
        print("Ошибка: тема не является словарём")
        return
    fixed_count = 0
    for i, theme in enumerate(themes):
        if 'title' not in theme or not theme['title']:
            theme['title'] = f'Tема {i+1}'
            fixed_count += 1
        if 'materials' not in theme or not isinstance(theme['materials'], list):
            theme['materials'] = []
            fixed_count += 1
        if 'checkpoints' not in theme or not isinstance(theme['checkpoints'], list):
            theme['checkpoints'] = []
            fixed_count += 1
    if fixed_count > 0:
        print(f"Исправлено {fixed_count} проблем в темах")
    if not all(isinstance(c, dict) for c in checkpoints):
        print("Ошибка: контрольная точка не является словарём")
        return
    for i, c in enumerate(checkpoints):
        if 'question' not in c or not c['question']:
            c['question'] = f'Вопрос {i+1}'
            fixed_count += 1
        if 'answer' not in c or not c['answer']:
            c['answer'] = 'Нет ответа'
            fixed_count += 1
    if fixed_count > 0:
        print(f"Исправлено {fixed_count} проблем в контрольных точках")
    if not all(isinstance(m, dict) for m in materials):
        print("Ошибка: материал не является словарём")
        return
    for i, m in enumerate(materials):
        if 'title' not in m or not m['title']:
            m['title'] = f'Материал {i+1}'
            fixed_count += 1
        if 'content' not in m or not m['content']:
            m['content'] = 'Нет контента'
            fixed_count += 1
    if fixed_count > 0:
        print(f"Исправлено {fixed_count} проблем в материалах")
    print("Проверка целостности завершена")
