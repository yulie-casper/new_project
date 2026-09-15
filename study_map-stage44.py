# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: StudyMap
def backup_data(filepath):
    """Создаёт резервную копию файла данных в директорию backup."""
    import shutil, os
    dir_path = os.path.dirname(filepath) or '.'
    backup_dir = os.path.join(dir_path, 'backup')
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = 'backup_' + datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, timestamp + os.path.basename(filepath))
    shutil.copy2(filepath, backup_path)
    return backup_path
