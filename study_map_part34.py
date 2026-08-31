# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: StudyMap
TEMPLATES = {
    "python": {
        "name": "Python",
        "color": "#3776AB",
        "tags": ["programming", "software"],
        "material": "https://python.org",
    },
    "math": {
        "name": "Math",
        "color": "#C00",
        "tags": ["logic", "science"],
        "material": "https://math.org",
    },
    "english": {
        "name": "English",
        "color": "#059863",
        "tags": ["language", "communication"],
        "material": "https://english.org",
    },
}

def add_from_template(template_name, record_id=None):
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    tpl = TEMPLATES[template_name]
    data = tpl.copy()
    if record_id:
        data["id"] = record_id
    return data
