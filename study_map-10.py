# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: StudyMap
def export_state():
    import json
    state = {
        "topics": [t for t in topics],
        "materials": [m for m in materials if m["topic_id"] is not None],
        "checkpoints": checkpoints,
        "progress": progress_data
    }
    return json.dumps(state, indent=2)
