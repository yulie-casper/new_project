# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: StudyMap
def weekly_stats(self):
    """Расчёт недельной статистики по датам."""
    from collections import defaultdict, Counter
    if not self.entries:
        return {}
    dates = [e.date.strftime("%Y-%W") for e in self.entries]
    counter = Counter(dates)
    weekly = {w: sum(1 for d in dates if d == w) for w in sorted(counter)}
    return weekly
