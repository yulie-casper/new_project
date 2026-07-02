# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: StudyMap
import json, os, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные обучения из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация структуры данных
        required_keys = ['topics', 'settings']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if not isinstance(data['topics'], list):
                raise TypeError("Поле 'topics' должно быть списком")
        
        # Преобразование данных в удобные структуры (если нужно)
        processed_topics = []
        for topic in data['topics']:
            if isinstance(topic, dict):
                processed_topics.append({
                    'id': topic.get('id'),
                    'title': topic.get('title', ''),
                    'materials': topic.get('materials', []),
                    'checkpoints': topic.get('checkpoints', [])
                })
        
        return {
            'topics': processed_topics,
            'settings': data['settings'],
            'version': 1.0
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (замените эту строку на ваш путь к файлу или вставьте содержимое напрямую)
if __name__ == "__main__":
    # Имитация загрузки из файла для демонстрации работы функции
    with open('initial_data.json', 'r', encoding='utf-8') as f:
        json_content = f.read()
    
    study_map_config = load_initial_data(json_content)
    print(f"Загружено тем: {len(study_map_config['topics'])}")
