# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: StudyMap
def validate_date(date_str):
    """Проверяет корректность даты в формате ДД.ММ.ГГГГ, возвращает отформатированную строку или сообщение об ошибке."""
    try:
        parts = date_str.strip().split('.')
        if len(parts) != 3 or not all(parts):
            return "Ошибка: неверный формат даты (ожидается ДД.ММ.ГГГГ)"
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= year <= 9999 and 1 <= month <= 12):
            return "Ошибка: некорректный год или месяц"
        days_in_month = [31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not (1 <= day <= days_in_month[month - 1]):
            return f"Ошибка: некорректный день для месяца {month}"
        return date_str.strip()
    except ValueError as e:
        return f"Ошибка: невозможна конвертация даты — {e}"
