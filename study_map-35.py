# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: StudyMap
def next_action(self, user: str, current_topic: str = None, progress: dict = None) -> str:
        """Рекомендует следующее действие на основе текущего состояния обучения."""
        if progress is None:
            progress = {}

        if current_topic:
            if current_topic in progress:
                if progress[current_topic] == 100:
                    return f"Тема {current_topic} завершена! Перейдите к следующей теме в плане."
                elif progress[current_topic] >= 80:
                    return f"Вы хорошо знаете {current_topic}. Практикуйте дополнительные задачи."
                else:
                    return f"Продолжайте изучать {current_topic}. Повторите основные концепции."
            else:
                return f"Начните изучение темы {current_topic} с базовых материалов."

        if not progress:
            return "Выберите тему для начала обучения."

        topics_done = sum(1 for v in progress.values() if v == 100)
        total = len(progress)
        if topics_done == total:
            return "Поздравляю! Вы прошли весь план обучения."
        if topics_done == 0:
            return "Начните с первой темы в плане."
        return f"Вы завершили {topics_done} из {total} тем. Выберите следующую тему."
