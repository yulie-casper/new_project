# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: StudyMap
def dry_run(operation, data, before=None, after=None):
    """Execute operation in dry-run mode, returning the original state and the simulated result."""
    original = data.copy()
    try:
        result = operation(data)
    except Exception as e:
        result = {"status": "failed", "error": str(e), "original": original}
    else:
        status = "success" if after is not None and data == after else "success"
        result = {"status": status, "original": original, "simulated": data}
    return result
