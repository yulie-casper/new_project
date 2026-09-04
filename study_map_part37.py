# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: StudyMap
import unittest


class TestStudyMap(unittest.TestCase):
    def test_add_topic(self):
        sm = StudyMap("Python Basics")
        sm.add_topic("Variables", "Learn types", "Done")
        topics = sm.get_topics()
        self.assertEqual(len(topics), 1)
        self.assertEqual(topics[0]["title"], "Variables")
        self.assertEqual(topics[0]["status"], "Done")

    def test_add_material(self):
        sm = StudyMap("Math")
        sm.add_topic("Algebra", "Intro", "In Progress")
        sm.add_material("Algebra", "Types", "text", "x + y")
        self.assertIn("Types", sm.get_materials("Algebra"))

    def test_add_checkpoint(self):
        sm = StudyMap("CS")
        sm.add_topic("Python", "Basics", "Done")
        sm.add_checkpoint("Python", "Basics", "Passed")
        checkpoints = sm.get_checkpoints("Python")
        self.assertEqual(len(checkpoints), 1)
        self.assertEqual(checkpoints[0]["status"], "Passed")

    def test_add_progress(self):
        sm = StudyMap("Web")
        sm.add_topic("HTML", "Intro", "Done")
        sm.add_progress("HTML", 100)
        progress = sm.get_progress("HTML")
        self.assertEqual(progress["progress"], 100)
        self.assertEqual(progress["status"], "Completed")

    def test_add_quiz(self):
        sm = StudyMap("JS")
        sm.add_topic("Functions", "Basics", "In Progress")
        sm.add_quiz("Functions", "Q1", "text", "What is a function?", "a", "a")
        quiz = sm.get_quiz("Functions")
        self.assertEqual(quiz["total"], 1)
        self.assertEqual(quiz["score"], 1)

    def test_add_schedule(self):
        sm = StudyMap("Study")
        sm.add_schedule("Monday", "HTML", "09:00", "10:00")
        schedule = sm.get_schedule()
        self.assertEqual(len(schedule), 1)
        self.assertEqual(schedule[0]["day"], "Monday")

    def test_add_note(self):
        sm = StudyMap("Notes")
        sm.add_note("Python", "Tip: use f-strings")
        notes = sm.get_notes("Python")
        self.assertEqual(len(notes), 1)
        self.assertIn("f-strings", notes[0])

    def test_add_milestone(self):
        sm = StudyMap("Goals")
        sm.add_milestone("Finish Python", 5, "Done")
        milestones = sm.get_milestones()
        self.assertEqual(len(milestones), 1)
        self.assertEqual(milestones[0]["status"], "Done")
