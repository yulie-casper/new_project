# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: StudyMap
def export_report():
    if not STUDY_DATA:
        print("Нет данных для отчёта. Сначала создайте план обучения.")
        return
    total_topics = sum(len(t.get("materials", [])) for t in STUDY_DATA["topics"])
    total_quizzes = sum(len(t.get("quizzes", [])) for t in STUDY_DATA["topics"])
    completed_quizzes = sum(
        q.get("completed", False) for t in STUDY_DATA["topics"] for q in t.get("quizzes", [])
    )
    completed_topics = sum(
        1 for t in STUDY_DATA["topics"] if t.get("completed", False)
    )
    progress = round(
        (completed_topics / len(STUDY_DATA["topics"])) * 100, 1
    ) if STUDY_DATA["topics"] else 0
    lines = ["StudyMap — краткий отчёт", "=" * 20, ""]
    lines.append(f"Общий прогресс: {progress}%")
    lines.append(f"Завершено тем: {completed_topics}/{len(STUDY_DATA['topics'])}")
    lines.append(f"Всего тем: {len(STUDY_DATA['topics'])}")
    lines.append("")
    lines.append("Детали по темам:")
    for topic in STUDY_DATA["topics"]:
        status = "готово" if topic.get("completed", False) else "в работе"
        lines.append(f"- {topic['title']} [{status}]")
        lines.append(f"    материалов: {len(topic.get('materials', []))}")
        lines.append(f"    контрольных: {len(topic.get('quizzes', []))}")
        done_q = sum(1 for q in topic.get("quizzes", []) if q.get("completed", False))
        lines.append(f"    пройдено контрольных: {done_q}/{len(topic.get('quizzes', []))}")
    lines.append("")
    report_text = "\n".join(lines)
    with open("studymap_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)
    print(report_text)
    print("\nОтчёт сохранён в studymap_report.txt")

export_report()
