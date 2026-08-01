# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: StudyMap
import json, os
from pathlib import Path


def reset_demo_data():
    """Сбрасывает демо-данные: удаляет все файлы проекта StudyMap."""
    project_dir = Path(__file__).parent
    demo_files = [
        "study_map.py",  # основной файл (неудаляем, т.к. это он)
    ]
    for f in ["data/topics.json", "data/materials.json",
              "data/milestones.json", "data/progress.json"]:
        fp = project_dir / f
        if fp.exists():
            fp.unlink()


def clear_state():
    """Очищает состояние приложения: удаляет файлы сессии и кеш."""
    state_files = [
        "state/session.json",
        "state/cache.json",
    ]
    for f in state_files:
        fp = Path(f)
        if fp.exists():
            fp.unlink()


if __name__ == "__main__":
    reset_demo_data()
    clear_state()
