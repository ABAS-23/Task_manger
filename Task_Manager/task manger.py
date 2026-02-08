tasks = []

def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    for index, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['title']} {status}")
    print()


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark.\n")
        return

    view_tasks(tasks)
    choice = int(input("Enter task number to mark as done: "))

    if 0 <= choice < len(tasks):
        tasks[choice]["done"] = True
        print("Task marked as done ✅\n")
    else:
        print("Invalid task number.\n")


def main_menu():
    while True:
        print("===========================")
        print("   SIMPLE TASK MANAGER")
        print("===========================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


main_menu()
