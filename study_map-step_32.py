# === Stage 32: Добавь журнал действий пользователя ===
# Project: StudyMap
class ActionLog:
    def __init__(self):
        self.actions = []

    def log(self, action_type, description):
        self.actions.append({"type": action_type, "description": description, "time": datetime.now().isoformat()})

    def get_recent(self, count=10):
        return self.actions[-count:]

    def get_by_type(self, action_type):
        return [a for a in self.actions if a["type"] == action_type]

    def get_stats(self):
        total = len(self.actions)
        by_type = {}
        for a in self.actions:
            by_type[a["type"]] = by_type.get(a["type"], 0) + 1
        return {"total": total, "by_type": by_type}
