# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: StudyMap
def print_metrics():
    total_topics = len(topics)
    completed_topics = sum(1 for t in topics if t.get("status") == "completed")
    pending_challenges = [ch for t in topics for ch in t.get("challenges", []) if not ch.get("done")]
    completed_challenges = sum(t.get("challenges", []), []).count(lambda x: x.get("done")) if hasattr(sum, 'count') else 0

    total_progress_points = sum(t.get("progress", {}).get("points", 0) for t in topics)
    max_possible_points = sum(max(ch.get("reward", 1) for ch in t.get("challenges", [])) * 3 for t in topics) if topics else 0

    print(f"📊 StudyMap Metrics:")
    print(f"   Topics: {completed_topics}/{total_topics}")
    print(f"   Challenges done: ~{max_possible_points - total_progress_points} remaining")
    print(f"   Total progress points earned: {total_progress_points}")
