# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: StudyMap
class ValidationError(Exception): pass

def validate_topic_input(topic_name: str, materials: list) -> None:
    if not topic_name or len(topic_name.strip()) < 2: raise ValidationError("Имя темы должно быть непустым и содержать минимум 2 символа.")
    for mat in materials:
        if not isinstance(mat, dict): raise ValidationError("Материал должен быть словарем.")
        if 'title' not in mat or 'content' not in mat: raise ValidationError("Каждый материал должен иметь поля title и content.")
        if len(str(mat['title'])) < 1: raise ValidationError("Заголовок материала не может быть пустым.")

def validate_checkpoint_input(checkpoint_name: str, questions: list) -> None:
    if not checkpoint_name or len(checkpoint_name.strip()) < 3: raise ValidationError("Имя контрольной точки должно содержать минимум 3 символа.")
    for q in questions:
        if 'question' not in q or 'options' not in q: raise ValidationError("Вопрос должен иметь поля question и options.")
        if len(q['options']) < 2: raise ValidationError("В списке вариантов ответа должно быть не менее двух элементов.")

def validate_user_progress_input(user_id: str, completed_topics: list) -> None:
    if not user_id or len(str(user_id).strip()) < 1: raise ValidationError("ID пользователя не может быть пустым.")
    for topic in completed_topics:
        if 'topic_name' not in topic or 'score' not in topic: raise ValidationError("Запись прогресса должна содержать topic_name и score.")
        if not isinstance(topic['score'], (int, float)) or topic['score'] < 0 or topic['score'] > 100: raise ValidationError("Оценка должна быть числом от 0 до 100.")

def sanitize_string(value: str) -> str:
    return value.strip().replace('\n', ' ').replace('  ', ' ')
