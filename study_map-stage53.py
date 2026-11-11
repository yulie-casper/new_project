# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: StudyMap
def import_records(path, fmt="records"):
    """
    Импортирует из простого текстового файла:
      fmt="records"   -> построчно: id,тема,уровень
      fmt="report"    -> построчно: дата;тема;уровень;пройден
    Возвращает список словарей. Пустые строки и #пропуск.
    """
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(";")]
            if fmt == "report" and len(parts) == 4:
                date, topic, level, done = parts
                records.append({
                    "date": date,
                    "topic": topic,
                    "level": int(level) if level.isdigit() else 0,
                    "done": done.lower() in ("1", "да", "true", "yes"),
                })
            elif len(parts) >= 2:
                topic, level = parts[0], parts[1]
                records.append({
                    "date": parts[2] if len(parts) > 2 else "",
                    "topic": topic,
                    "level": int(level) if level.isdigit() else 0,
                    "done": False,
                })
    return records
