# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: StudyMap
def add_favorite(note_id):
    try:
        note = next(n for n in notes if n["id"] == note_id)
    except StopIteration:
        return
    if note_id not in favorites:
        favorites.append(note_id)
        save()
def show_favorites():
    if not favorites:
        print("Избранных записей пока нет.")
        return
    print("=== Избранные записи ===")
    for note_id in favorites:
        note = next(n for n in notes if n["id"] == note_id)
        print(f'{note["id"]}: {note["title"]} — {note["content"]}')
