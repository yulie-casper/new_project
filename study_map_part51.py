# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: StudyMap
import json
from datetime import datetime

class DataJournal:
    def __init__(self, path="journal.json"):
        self.path = path
        self.entries = []
        self._load()
    
    def _load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.entries = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []
    
    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)
    
    def log(self, action, data):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "data": data
        }
        self.entries.append(entry)
        self._save()
    
    def get_changes(self):
        return self.entries
