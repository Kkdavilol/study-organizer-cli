import json
import os

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def add_task(task):
    if not task:
        raise ValueError("Task cannot be empty")

    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i + 1}. [{status}] {t['task']}")


def complete_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid index")

    tasks[index]["done"] = True
    save_tasks(tasks)


def remove_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid index")

    tasks.pop(index)
    save_tasks(tasks)


def menu():
    while True:
        print("\nStudy Organizer CLI")
        print("1 - Add Task")
        print("2 - List Tasks")
        print("3 - Complete Task")
        print("4 - Remove Task")
        print("5 - Exit")

        choice = input("> ")

        if choice == "1":
            task = input("Task: ")
            add_task(task)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            index = int(input("Task number: ")) - 1
            complete_task(index)

        elif choice == "4":
            index = int(input("Task number: ")) - 1
            remove_task(index)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
