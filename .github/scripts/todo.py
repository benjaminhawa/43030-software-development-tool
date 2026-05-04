class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        t1 = Task("Buy groceries")
        t2 = Task("Write report")
        t3 = Task("Call dentist")
        t4 = Task("Fix bug #42")
        t5 = Task("Read chapter 5")
        t6 = Task("Clean desk")
        t1.mark_completed()
        t2.mark_completed()
        t3.mark_completed()
        self.tasks = [t1, t2, t3, t4, t5, t6]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    open_tasks = [t.title for t in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in open_tasks:
        print(title)

    done_tasks = [t.title for t in pool.get_done_tasks()]
    print("Done Tasks:")
    for title in done_tasks:
        print(title)


if __name__ == "__main__":
    main()
