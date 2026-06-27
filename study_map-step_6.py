# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: StudyMap
def filter_records(query=None, status=None, category=None, tags=None):
    if query:
        records = [r for r in records if query.lower() in str(r.get('title', '')).lower()]
    if status is not None:
        records = [r for r in records if r.get('status') == status]
    if category:
        records = [r for r in records if r.get('category') == category]
    if tags:
        record_tags = lambda r: set(r.get('tags', [])).intersection(set(tags.split()))
        records = [r for r in records if record_tags(r)]
    return records
