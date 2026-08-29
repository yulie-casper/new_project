# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: StudyMap
class UndoManager:
    def __init__(self):
        self._stack = []

    def push(self, action):
        self._stack.append(action)

    def undo(self):
        if not self._stack:
            return None
        action = self._stack.pop()
        if hasattr(action, 'undo'):
            result = action.undo()
        else:
            result = action()
        return result

    def is_empty(self):
        return len(self._stack) == 0

    def clear(self):
        self._stack.clear()
