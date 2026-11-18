# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: StudyMap
def bulk_update(selected_ids, new_status, new_tags=None):
    updated = []
    for item in records:
        if item["id"] in selected_ids:
            if new_status is not None:
                item["status"] = new_status
            if new_tags:
                existing = item.get("tags", [])
                merged = list(dict.fromkeys(existing + new_tags))
                item["tags"] = merged
            updated.append(item["id"])
    return updated
