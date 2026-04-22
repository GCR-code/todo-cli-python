"""
To-Do CLI Application
---------------------
A command-line task manager with features:
- Add, edit, delete tasks
- Mark tasks as done
- Filter tasks
- Save/load tasks from file
- Export tasks to text file

Author: Chathil Rajarathna
"""

tasks = []


# LOAD TASKS
def load_tasks():
    tasks.clear()
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    continue

                name, done, priority = parts
                tasks.append({
                    "name": name,
                    "done": done == "True",
                    "priority": priority
                })

        print(f"Loaded {len(tasks)} task(s)." if tasks else "No tasks found.")
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")


# SAVE TASKS
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['done']}|{task['priority']}\n")


# GET PRIORITY
def get_priority():
    while True:
        p = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if p in ["High", "Medium", "Low"]:
            return p
        print("Invalid priority")


# VIEW TASKS
def view_tasks(task_list=None):
    if task_list is None:
        task_list = tasks

    if not task_list:
        print("No tasks available")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(task_list, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['name']} ({task['priority']})")


# ADD TASK
def add_task():
    while True:
        task_name = input('Enter task or "back": ').strip()

        if task_name.lower() == 'back':
            return

        if not task_name:
            print("Task cannot be empty")
            continue

        if any(t["name"].lower() == task_name.lower() for t in tasks):
            print("Task already exists!")
            continue

        priority = get_priority()

        tasks.append({
            "name": task_name,
            "done": False,
            "priority": priority
        })

        save_tasks()
        print(f'Task "{task_name}" added\n')


# EDIT TASK
def edit_task():
    if not tasks:
        print("No tasks available")
        return

    view_tasks()

    while True:
        choice = input('Enter task number or "back": ').strip()

        if choice.lower() == 'back':
            return

        if not choice.isdigit():
            print("Invalid input")
            continue

        index = int(choice) - 1

        if 0 <= index < len(tasks):
            task = tasks[index]

            new_name = input(f'New name (Enter to keep "{task["name"]}"): ').strip()
            if new_name:
                task["name"] = new_name

            if input("Change priority? (yes/no): ").strip().lower() == "yes":
                task["priority"] = get_priority()

            save_tasks()
            print("Task updated\n")
            return
        else:
            print("Invalid number")


# MARK DONE
def mark_done():
    if not tasks:
        print("No tasks available")
        return

    view_tasks()

    while True:
        choice = input('Enter number or "back": ').strip()

        if choice.lower() == 'back':
            return

        if not choice.isdigit():
            print("Invalid input")
            continue

        index = int(choice) - 1

        if 0 <= index < len(tasks):
            if tasks[index]["done"]:
                print("Task already completed")
                return

            tasks[index]["done"] = True
            save_tasks()
            print("Task marked as done\n")
            return
        else:
            print("Invalid number")


# DELETE TASK
def delete_task():
    if not tasks:
        print("No tasks to delete")
        return

    view_tasks()

    while True:
        choice = input('Enter number or "back": ').strip()

        if choice.lower() == 'back':
            return

        if not choice.isdigit():
            print("Invalid input")
            continue

        index = int(choice) - 1

        if 0 <= index < len(tasks):
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm != "yes":
                return

            removed = tasks.pop(index)
            save_tasks()
            print(f'Task "{removed["name"]}" deleted\n')
            return
        else:
            print("Invalid number")


# FILTER TASKS
def filter_tasks():
    if not tasks:
        print("No tasks available")
        return

    print("\n1. Completed")
    print("2. Pending")
    print("3. By Priority")

    choice = input("Choose filter: ").strip()

    if choice == "1":
        filtered = [t for t in tasks if t["done"]]
    elif choice == "2":
        filtered = [t for t in tasks if not t["done"]]
    elif choice == "3":
        p = get_priority()
        filtered = [t for t in tasks if t["priority"] == p]
    else:
        print("Invalid choice")
        return

    view_tasks(filtered)


# RESET TASKS
def reset_tasks():
    if not tasks:
        print("No tasks to reset")
        return

    if input("Delete ALL tasks? (yes/no): ").strip().lower() == "yes":
        tasks.clear()
        save_tasks()
        print("All tasks deleted.\n")


# EXPORT TASKS
def export_tasks():
    if not tasks:
        print("No tasks to export.")
        return

    filename = input("Enter file name: ").strip()
    if not filename:
        return

    filename += ".txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== TO-DO LIST ===\n\n")

        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            file.write(f"{i}. [{status}] {task['name']} ({task['priority']})\n")

    print("Exported successfully\n")


# MAIN PROGRAM
def main():
    load_tasks()

    while True:
        print('\n=== TO-DO LIST ===')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Edit Task')
        print('4. Mark Task as Done')
        print('5. Delete Task')
        print('6. Filter Tasks')
        print('7. Reset Task List')
        print('8. Export Tasks')
        print('9. Exit')

        try:
            choice = int(input('Enter choice: '))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                edit_task()
            elif choice == 4:
                mark_done()
            elif choice == 5:
                delete_task()
            elif choice == 6:
                filter_tasks()
            elif choice == 7:
                reset_tasks()
            elif choice == 8:
                export_tasks()
            elif choice == 9:
                print("Exiting program.")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Enter a valid number")


if __name__ == "__main__":
    main()