# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: StudyMap
import json, os

def load_profile():
    path = os.path.join(os.path.dirname(__file__), "profiles.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"users": {}}

def save_profile(profiles):
    path = os.path.join(os.path.dirname(__file__), "profiles.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)

def switch_profile(name):
    profiles = load_profile()
    if name not in profiles["users"]:
        profiles["users"][name] = {"topics": [], "mastery": {}, "active": False}
        save_profile(profiles)
    else:
        profiles["users"][name]["active"] = True
        save_profile(profiles)
    return profiles["users"][name]
