
tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - {status}")


def add_task():
    name = input("Enter your task: ")
    tasks.append({"name": name, "completed": False})
    print("Task added successfully!")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
        tasks[number - 1]["completed"] = True
        print("Task completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")


while True:
    print("\n===== MY TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
