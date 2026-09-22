# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: StudyMap
import hashlib, json, os, random
from datetime import datetime

class Checkpoint:
    def __init__(self, topic, criteria, score=0, max_score=10):
        self.topic = topic
        self.criteria = criteria
        self.score = score
        self.max_score = max_score

    def progress(self):
        return self.score / self.max_score if self.max_score else 0

    def pass_threshold(self):
        return self.score >= self.max_score * 0.8

class ProgressTracker:
    def __init__(self):
        self.checkpoints = {}
        self.last_check = datetime.now()

    def add_checkpoint(self, checkpoint):
        self.checkpoints[checkpoint.topic] = checkpoint

    def update(self, topic, score):
        if topic in self.checkpoints:
            self.checkpoints[topic].score = min(score, self.checkpoints[topic].max_score)
            self.last_check = datetime.now()

    def get_status(self):
        return {t: c.progress() for t, c in self.checkpoints.items()}

    def save(self, path="studymap_progress.json"):
        data = {t: {"score": c.score, "max_score": c.max_score, "passed": c.pass_threshold()} for t, c in self.checkpoints.items()}
        data["last_check"] = self.last_check.isoformat()
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, path="studymap_progress.json"):
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            for topic, info in data.items():
                if topic != "last_check":
                    cp = Checkpoint(topic, "", info.get("score", 0), info.get("max_score", 10))
                    self.checkpoints[topic] = cp
            self.last_check = datetime.fromisoformat(data.get("last_check", ""))
