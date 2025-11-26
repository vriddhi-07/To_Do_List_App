import os
from todo import add_task, list_tasks, load_todos, save_todos, TODO_FILE


def setup_function():
    # Before each test, ensure empty file
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)


def test_add_task_creates_file_and_adds():
    add_task("Test task")
    todos = load_todos()
    assert "Test task" in todos


def test_save_and_load_todos():
    tasks = ["Task 1", "Task 2"]
    save_todos(tasks)
    loaded = load_todos()
    assert loaded == tasks
