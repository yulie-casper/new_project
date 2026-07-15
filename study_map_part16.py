# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: StudyMap
def monthly_stats(self):
    """Calculate statistics grouped by month from the history of study sessions."""
    if not self.history:
        return []
    
    stats = {}
    for session in sorted(self.history, key=lambda s: s['date']):
        date_str = session['date'][:7]  # Extract YYYY-MM
        if date_str not in stats:
            stats[date_str] = {'sessions': 0, 'hours': 0.0}
        stats[date_str]['sessions'] += 1
        stats[date_str]['hours'] += self._get_session_duration(session)

    return [{'month': k, **v} for k, v in sorted(stats.items())]


def _get_session_duration(self, session):
    """Calculate duration of a study session based on start and end times."""
    try:
        start = datetime.strptime(session['start_time'], '%H:%M')
        end = datetime.strptime(session['end_time'], '%H:%M')
        delta = end - start
        return delta.total_seconds() / 3600.0
    except (KeyError, ValueError):
        return session.get('duration', 1.0)


StudyMap.monthly_stats = monthly_stats
StudyMap._get_session_duration = _get_session_duration
