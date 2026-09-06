# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: StudyMap
def test_edge_cases():
        sm = StudyMap("Test")
        sm.add_topic("Python", ["intro", "loops", "functions"])
        assert sm.get_topic("Python") == {"name": "Python", "materials": ["intro", "loops", "functions"], "checkpoints": [], "progress": {}}
        assert sm.get_topic("nonexistent") is None
        sm.add_checkpoint("Python", "intro", "Basic Python")
        assert sm.get_checkpoint("Python", "intro") == "Basic Python"
        sm.add_checkpoint("Python", "intro", "Advanced Python")
        assert sm.get_checkpoint("Python", "intro") == "Advanced Python"
        assert sm.get_checkpoint("Python", "nonexistent") is None
        sm.add_material("Python", "intro", "Python Textbook")
        assert sm.get_material("Python", "intro") == "Python Textbook"
        sm.add_material("Python", "intro", "Python Online Course")
        assert sm.get_material("Python", "intro") == "Python Online Course"
        sm.add_material("Python", "nonexistent", "Fake Material")
        assert sm.get_material("Python", "nonexistent") is None
        sm.add_checkpoint("Python", "nonexistent", "Fake Checkpoint")
        assert sm.get_checkpoint("Python", "nonexistent") is None
        sm.add_material("nonexistent", "intro", "Fake Material 2")
        assert sm.get_material("nonexistent", "intro") is None
        sm.add_checkpoint("nonexistent", "intro", "Fake Checkpoint 2")
        assert sm.get_checkpoint("nonexistent", "intro") is None
        assert sm.get_progress("Python") == {"intro": 0.0, "loops": 0.0, "functions": 0.0}
        assert sm.get_progress("nonexistent") is None
        sm.add_checkpoint("Python", "loops", "Loop Mastery")
        sm.add_checkpoint("Python", "functions", "Function Mastery")
        assert sm.get_progress("Python") == {"intro": 0.0, "loops": 1.0, "functions": 1.0}
        sm.add_checkpoint("Python", "intro", "Intro Mastery")
        assert sm.get_progress("Python") == {"intro": 1.0, "loops": 1.0, "functions": 1.0}
        assert sm.get_overall_progress() == 1.0
        assert sm.get_overall_progress() == 100.0
        assert sm.get_overall_progress() == 1.0
