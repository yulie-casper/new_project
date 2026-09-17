# === Stage 45: Добавь восстановление из резервной копии ===
# Project: StudyMap
def restore_backup(backup_path):
    """Восстановить данные из резервной копии."""
    if not os.path.exists(backup_path):
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        global topics, materials, checkpoints, progress
        topics = backup_data.get('topics', [])
        materials = backup_data.get('materials', [])
        checkpoints = backup_data.get('checkpoints', [])
        progress = backup_data.get('progress', {})
        return True
    except Exception:
        return False
