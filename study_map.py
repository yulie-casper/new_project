# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: StudyMap
import json
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Topic:
    id: int
    title: str
    materials: list[str] = field(default_factory=list)
    checkpoints: list[dict] = field(default_factory=list)

@dataclass
class UserProgress:
    completed_topics: set[int] = field(default_factory=set)
    current_topic_id: Optional[int] = None

def init_study_map():
    topics = [
        Topic(1, "Введение в Python", ["Базовая синтаксис", "Типы данных"]),
        Topic(2, "Структуры данных", ["Списки и словари", "Наборы"]),
        Topic(3, "Программирование на объектах", ["Классы и наследование"])
    ]
    progress = UserProgress()
    with open("study_map.json", "w", encoding="utf-8") as f:
        json.dump({"topics": [t.__dict__ for t in topics], "progress": progress.__dict__, "__version__": 1}, f, ensure_ascii=False)

if __name__ == "__main__":
    init_study_map()
