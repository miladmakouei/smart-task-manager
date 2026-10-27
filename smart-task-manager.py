
import json
from datetime import datetime

FILE_NAME = "tasks.json"
PRIORITIES = ["Low", "Medium", "High"]


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid data.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(tasks):
    title = input("Task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    print("\nSelect priority:")
    for index, priority in enumerate(PRIORITIES, start=1):
        print(f"{index}. {priority}")

    choice = input("Priority number: ")

    try:
        priority_index = int(choice) - 1
        priority = PRIORITIES[priority_index]
    except (ValueError, IndexError):
        print("Invalid priority.")
        return

    next_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task #{next_id} added successfully.")


def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task List ---")

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"

        print(
            f"ID: {task['id']} | "
            f"{task['title']} | "
            f"Priority: {task['priority']} | "
            f"Status: {status} | "
            f"Created: {task['created_at']}"
        )


def complete_task(tasks):
    task_id = input("Enter task ID to complete: ")

    try:
        task_id = int(task_id)
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task completed successfully.")
            return

    print("Task ID not found.")


def filter_tasks(tasks):
    print("\n1. Show pending tasks")
    print("2. Show completed tasks")
    print("3. Show high-priority tasks")

    choice = input("Choose a filter: ")

    if choice == "1":
        results = [
            task for task in tasks
            if not task["completed"]
        ]
    elif choice == "2":
        results = [
            task for task in tasks
            if task["completed"]
        ]
    elif choice == "3":
        results = [
            task for task in tasks
            if task["priority"] == "High"
            and not task["completed"]
        ]
    else:
        print("Invalid filter.")
        return

    show_tasks(results)


def show_report(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    high_priority = sum(
        1 for task in tasks
        if task["priority"] == "High"
        and not task["completed"]
    )

    print("\n--- Task Report ---")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"Pending high-priority tasks: {high_priority}")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== SMART TASK MANAGER =====")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Complete a task")
        print("4. Filter tasks")
        print("5. Show report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            filter_tasks(tasks)
        elif choice == "5":
            show_report(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
