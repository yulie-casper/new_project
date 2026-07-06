# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: StudyMap
import json


def load_studymap(path="studymap.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON structure must be a top-level object")
        return data
    except FileNotFoundError:
        print(f"File {path} not found. Creating default structure.")
        return {"topics": [], "progress": {}, "milestones": []}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}")
        raise
