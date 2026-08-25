# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: StudyMap
def add_profile_support():
    class Profile:
        def __init__(self, name, topics=None, progress=None):
            self.name = name
            self.topics = topics or {}
            self.progress = progress or {}

    profiles = {}
    active_profile = None

    def get_profile(name):
        return profiles.get(name, Profile(name))

    def set_active_profile(name):
        nonlocal active_profile
        profile = get_profile(name)
        profiles[name] = profile
        active_profile = profile
        return profile

    def show_profile(name):
        profile = get_profile(name)
        print(f"\nПрофиль: {profile.name}")
        print(f"  Темы: {profile.topics}")
        print(f"  Прогресс: {profile.progress}")

    def add_topic_for_profile(name, topic_id, topic_data):
        profile = get_profile(name)
        profile.topics[topic_id] = topic_data
        return profile

    def set_progress_for_profile(name, topic_id, progress_value):
        profile = get_profile(name)
        profile.progress[topic_id] = progress_value
        return profile

    def list_profiles():
        print("\nДоступные профили:")
        for name in profiles:
            print(f"  - {name}")
        if active_profile:
            print(f"  Активен: {active_profile.name}")
