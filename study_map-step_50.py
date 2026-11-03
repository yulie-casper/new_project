# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: StudyMap
def format_status_line(progress: float, completed: int, total: int) -> str:
    percent = round(progress * 100)
    bar_len = 20
    filled = int(bar_len * progress)
    bar = "#" * filled + "-" * (bar_len - filled)
    return (f"Прогресс: {percent}%  |  [{bar}]  "
            f"({completed}/{total} тем завершено)")


def render_completion_message(topic_name: str, points: int) -> str:
    plural = "очков" if points != 1 else "очко"
    if points == 0:
        plural = "очков"
    return f"Поздравляем! Тема «{topic_name}» успешно завершена. " \
           f"Вы заработали {points} {plural}."


def render_progress_report(progress: float,
                          topics: list[str],
                          completed: list[str]) -> str:
    lines = [f"Отчёт по обучению", "=" * 20]
    for topic in topics:
        status = "✓" if topic in completed else "·"
        lines.append(f"{status} {topic}")
    lines.append("=" * 20)
    lines.append(format_status_line(progress, len(completed), len(topics)))
    return "\n".join(lines)
