# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: StudyMap
def generate_summary():
    """Генерирует краткую сводку по текущим данным."""
    topics = data.get("topics", [])
    if not topics:
        return "Нет данных для сводки."

    summary_parts = []
    for t in topics[:10]:  # Ограничиваем до 10 тем
        name = t.get("name", "Неизвестная тема")
        status = t.get("status", "не изучена")
        progress = t.get("progress", 0)

        if status == "completed":
            summary_parts.append(f"✅ {name} — завершена (100%)")
        elif status == "in_progress":
            summary_parts.append(f"📚 {name} — прогресс: {progress}%")
        else:
            summary_parts.append(f"⬜ {name} — не начата")

    return "\n".join(summary_parts)

# Пример использования:
print(generate_summary())
