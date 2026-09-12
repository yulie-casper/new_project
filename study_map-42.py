# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: StudyMap
import sys

def _is_color_enabled():
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

def _colorize(text, color_code):
    if not _is_color_enabled():
        return text
    return f"\033[{color_code}m{text}\033[0m"

def _red(text): return _colorize(text, 31)
def _green(text): return _colorize(text, 32)
def _yellow(text): return _colorize(text, 33)
def _blue(text): return _colorize(text, 34)
def _cyan(text): return _colorize(text, 36)
def _magenta(text): return _colorize(text, 35)
def _white(text): return _colorize(text, 37)

def _section(title):
    print(_cyan("=" * 60))
    print(_cyan(f"  {title}"))
    print(_cyan("=" * 60))
