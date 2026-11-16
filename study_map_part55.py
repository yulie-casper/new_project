# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: StudyMap
def _dedupe_data(data, key_field, existing):
    for item in existing:
        if item.get(key_field) == data.get(key_field):
            return data, False
    return data, True

def add_with_dedupe(model, key_field, data):
    existing = _get_all(model)
    new_data, is_new = _dedupe_data(data, key_field, existing)
    if not is_new:
        return None, False
    record = new_record(model, new_data)
    _save(record)
    return record, True
