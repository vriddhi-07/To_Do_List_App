import sys

TODO_FILE = "todos.txt"


def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for t in todos:
            f.write(t + "\n")


def add_task(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added: {task}")


def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks yet!")
    else:
        for i, t in enumerate(todos, start=1):
            print(f"{i}. {t}")


def remove_task(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"Removed: {removed}")
    else:
        print("Invalid index.")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python todo.py add \"task description\"")
        print("  python todo.py list")
        print("  python todo.py remove INDEX")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            sys.exit(1)
        task = " ".join(sys.argv[2:])
        add_task(task)

    elif command == "list":
        list_tasks()

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Please provide the index to remove.")
            sys.exit(1)
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("Index must be an integer.")
            sys.exit(1)
        remove_task(index)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
