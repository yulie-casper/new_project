# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: StudyMap
import json, os

MIGRATION_VERSION = 2

def migrate_study_map(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid StudyMap data format")
    if data.get('version') < MIGRATION_VERSION:
        new = {'version': MIGRATION_VERSION, 'topics': {}, 'progress': {}, 'checkpoints': []}
        for topic, info in data.get('topics', {}).items():
            if isinstance(info, dict):
                new['topics'][topic] = {k: v for k, v in info.items() if k != 'version'}
            else:
                new['topics'][topic] = info
        for topic, progress in data.get('progress', {}).items():
            new['progress'][topic] = progress
        for cp in data.get('checkpoints', []):
            new['checkpoints'].append(cp)
        return new
    return data
