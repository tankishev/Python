# The Section class should receive a name (string) upon initialization.
# The task also has one instance attribute: tasks (empty list)
# The Section class should also have four methods:
# -	add_task(new_task: Task)
# o	Adds a new task to the collection and returns "Task {task details} is added to the section"
# o	If the task is already in the collection, returns "Task is already in the section {section_name}"
# -	complete_task(task_name: str)
# o	Changes the task to completed (True) and returns "Completed task {task_name}"
# o	If the task is not found, returns "Could not find task with the name {task_name}"
# -	clean_section()
# o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
# -	view_section()
# o	Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"
from .task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        else:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        task = None
        for t in self.tasks:
            if t.name == task_name:
                task = t
                break

        if task:
            task.completed = True
            return f'Completed task {task_name}'
        else:
            return f'Could not find task with the name {task_name}'

    def clean_section(self) -> str:
        i = 0
        for task in [t for t in self.tasks if t.completed is True]:
            self.tasks.pop(self.tasks.index(task))
            i += 1
        return f'Cleared {i} tasks.'

    def view_section(self) -> str:
        retval = f"Section {self.name}:"
        if self.tasks:
            retval += '\n' + '\n'.join([task.details() for task in self.tasks])
        return retval
