# === Stage 20: Добавь восстановление записей из архива ===
# Project: StudyMap
import json, os, shutil

def restore_records(archive_path):
    """Восстанавливает записи из архива в текущую базу данных."""
    if not archive_path or not os.path.exists(archive_path):
        print(f"Архив не найден: {archive_path}")
        return False
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            records = json.load(f)
        if not isinstance(records, list):
            print("Некорректный формат архива")
            return False
        db_file = os.path.join(os.path.dirname(__file__), 'study_map_db.json')
        backup_path = db_file + '.backup'
        shutil.copy2(db_file, backup_path) if os.path.exists(db_file) else None
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=4)
        print(f"Восстановлено {len(records)} записей из архива")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        if os.path.exists(backup_path):
            shutil.move(backup_path, db_file)
        return False
