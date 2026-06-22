# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: StudyMap
class StudyMap:
    def __init__(self):
        self._topics = []
        self._materials = {}
        self._checks = {}
        self._progress = {}

    def add_topic(self, name: str, description: str) -> None:
        topic_id = len(self._topics) + 1
        self._topics.append({"id": topic_id, "name": name, "description": description})

    def add_material(self, topic_name: str, content: str) -> None:
        for t in self._topics:
            if t["name"] == topic_name:
                self._materials[t["id"]] = {"topic_name": topic_name, "content": content}
                break

    def add_check(self, topic_name: str, question: str, correct_answer: str) -> None:
        for t in self._topics:
            if t["name"] == topic_name:
                self._checks[t["id"]] = {"topic_name": topic_name, "question": question, "correct_answer": correct_answer}
                break

    def mark_progress(self, topic_name: str) -> None:
        for t in self._topics:
            if t["name"] == topic_name:
                self._progress[t["id"]] = {"completed": True, "date": datetime.now().isoformat()}
                break
