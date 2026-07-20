# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: StudyMap
import copy, time

def archive_entry(entry):
    """Archive a study entry: mark it complete and move to an archive dict."""
    if not isinstance(entry, dict) or 'id' not in entry:
        return None
    archived = {**entry, **{'archived': True, 'archive_time': time.time()}}
    return copy.deepcopy(archived)

def get_archive_list(entries):
    """Return a list of all archived entries."""
    return [e for e in entries if isinstance(e, dict) and e.get('archived')]

def remove_archived(entry):
    """Remove an entry from the archive (restore it as active)."""
    if not isinstance(entry, dict) or 'id' not in entry:
        return None
    archived = copy.deepcopy(entry)
    archived['archived'] = False
    archived['archive_time'] = 0.0
    return archived

def process_entries(entries):
    """Archive entries where progress is >= 100% or older than archive_threshold days."""
    threshold_days = getattr(process_entries, 'archive_threshold', 365) / (24 * 3600)
    for i in range(len(entries)):
        e = entries[i]
        if isinstance(e, dict) and e.get('archived'):
            continue
        progress = e.get('progress', 0)
        created = e.get('created_at', 0)
        now = time.time()
        if (progress >= 100) or (now - created > threshold_days):
            entries[i] = archive_entry(e)
    return entries

def get_archive_stats(entries):
    """Return count of active vs archived entries."""
    active = sum(1 for e in entries if isinstance(e, dict) and not e.get('archived'))
    archived = len([e for e in entries if isinstance(e, dict) and e.get('archived')])
    return {'active': active, 'archived': archived}

def restore_from_archive(entry):
    """Restore a previously archived entry back to active state."""
    if not isinstance(entry, dict) or not entry.get('archived'):
        return None
    restored = remove_archived(entry)
    return copy.deepcopy(restored)
