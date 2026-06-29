# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: StudyMap
def sort_records(records, key='date'):
    if not records: return []
    reverse = {'date': False, 'priority': True, 'name': False}[key]
    return sorted(records, key=lambda r: (r.get(key) or 0), reverse=reverse)
