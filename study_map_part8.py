# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: StudyMap
def main():
    import os, sys
    from datetime import datetime
    if not hasattr(sys.modules[__name__], 'app'): app = {}
    def save():
        data = {'topics': app.get('topics', []), 'progress': app.get('progress', {})}
        with open('study_map.json', 'w') as f: json.dump(data, f)
    if os.path.exists('study_map.json'):
        import json; app['topics'] = json.load(open('study_map.json')).get('topics', [])
        app['progress'] = json.load(open('study_map.json')).get('progress', {})
    else:
        app['topics'] = [{'id': 1, 'title': 'Введение в Python', 'materials': ['Базовая синтаксис'], 'checks': []}]
        save()
    print("\n=== StudyMap v0.8 ===")
    while True:
        try:
            cmd = input("Команда (1-5, q=выход): ").strip().lower()
            if not cmd or cmd == 'q': break
            elif cmd in ['1', '2']: print(f"Темы: {app['topics']}")
            elif cmd == '3' and app['progress']: print("Прогресс:", list(app['progress'].keys()))
            elif cmd == '4': save(); print("Сохранено!")
            else: print("Неизвестная команда.")
        except KeyboardInterrupt: break

if __name__ == '__main__': main()
