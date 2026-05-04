import unittest
import sys
from io import StringIO
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Test task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertIn("Fix bug #42", [t.title for t in open_tasks])
        self.assertIn("Read chapter 5", [t.title for t in open_tasks])
        self.assertIn("Clean desk", [t.title for t in open_tasks])

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertIn("Buy groceries", [t.title for t in done_tasks])
        self.assertIn("Write report", [t.title for t in done_tasks])
        self.assertIn("Call dentist", [t.title for t in done_tasks])

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTaskPool)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    runner.run(suite)
    output = stream.getvalue().splitlines()
    for line in output:
        if "... ok" in line:
            print(line.split(" ... ")[0].split(".")[-1] + " ... ok")
