# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: StudyMap
import json

def print_topic_summary(topic):
    """Print a compact summary of a single topic with key details."""
    print(f"Topic: {topic['name']}")
    print(f"- ID:      {topic.get('id', 'N/A')}")
    print(f"- Level:   {'★' * (int(topic.get('level', 1)))}{'☆' * max(0, 5 - int(topic.get('level', 1)))}")
    print(f"- Status:  {'✅ Done' if topic.get('done') else '🔄 In Progress'}")
    print(f"- Topics covered: {topic.get('topics_covered', [])[:3]}{'...' if len(topic.get('topics_covered', [])) > 3 else ''}")
    if topic.get('summary'):
        print(f"- Summary: {topic['summary'][:100]}")
    resources = topic.get('resources', [])
    if resources:
        print(f"- Resources: {len(resources)} items ({', '.join(r.get('title','') for r in resources[:2])})")
    checks = topic.get('checks', [])
    if checks:
        passed = sum(1 for c in checks if c.get('passed'))
        total = len(checks)
        print(f"- Checks: {passed}/{total} passed")
