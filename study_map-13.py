# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: StudyMap
def search_across_fields(text, fields):
    """Search text case-insensitively across multiple fields."""
    normalized = [text.lower() for field in fields if field]
    return any(field.lower() in normalized for field in fields)
