# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: StudyMap
def print_study_table(study_plan):
    if not study_plan:
        return
    headers = ["#", "Тема", "Статус", "Прогресс"]
    col_widths = [2, 30, 15, 12]
    # Заголовки с разделителями
    separator = "+" + "+".join("-" * (w) for w in col_widths) + "+"
    header_row = "|" + "|".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + "|"
    print(separator)
    print(header_row)
    print(separator)
    for idx, topic in enumerate(study_plan):
        status_map = {"done": "✅", "in_progress": "🔄", "planned": "⏳"}
        status = status_map.get(topic["status"], "?")
        progress_str = f"{topic['progress']}%" if topic["progress"] else "—"
        row = "|" + "|".join([str(idx+1), str(topic["title"]), status, progress_str]) + "|"
        print(row)
    print(separator)
