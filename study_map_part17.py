# === Stage 17: Добавь группировку записей по категориям ===
# Project: StudyMap
def group_by_category(records):
        groups = {}
        for rec in records:
            cat = rec.get("category", "uncategorized")
            groups.setdefault(cat, []).append(rec)
        return dict(sorted(groups.items()))
