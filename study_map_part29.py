# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: StudyMap
# StudyMap Configuration via Settings Dictionary
SETTINGS = {
    "app_name": "StudyMap",
    "version": 29,
    "default_theme_count": 5,
    "max_attempts_per_topic": 3,
    "progress_save_interval_sec": 60,
    "language": "ru",
}

def load_settings():
    return SETTINGS.copy()

def update_setting(key, value):
    if key in SETTINGS:
        SETTINGS[key] = value
    else:
        raise KeyError(f"Unknown setting key: {key}")

settings = load_settings()
