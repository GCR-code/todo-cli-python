# 📝 To-Do CLI (Python)

A lightweight command-line task manager built with Python. Manage your tasks directly from the terminal with persistent storage and no external dependencies.

---

## ✨ Features

* Add tasks with priority levels (High, Medium, Low)
* View tasks in a clean numbered list
* Edit tasks (rename or change priority)
* Mark tasks as completed
* Delete tasks with confirmation
* Filter tasks by status or priority
* Reset the entire task list
* Export tasks to a `.txt` file
* Persistent storage (auto save & load)

---

## 📋 Requirements

* Python 3.x

---

## 🚀 Installation

```bash
git clone https://github.com/gcr-code/todo-cli-python.git
cd todo-cli-python
```

---

## ▶️ Run

```bash
python todo_cli.py
```

---

## 🖥️ Usage

On launch, you'll see the main menu:

```
=== TO-DO LIST ===
1. Add Task
2. View Tasks
3. Edit Task
4. Mark Task as Done
5. Delete Task
6. Filter Tasks
7. Reset Task List
8. Export Tasks
9. Exit
```

Enter the number corresponding to the action you want.
Tasks are automatically saved to `tasks.txt`.

---

## 📌 Example

```
Enter choice: 1
Enter task or "back": Buy groceries
Enter priority (High/Medium/Low): High
Task "Buy groceries" added

Your Tasks:
1. [ ] Buy groceries (High)
```

---

## 📂 File Storage

Tasks are stored in `tasks.txt` using a simple format:

```
Buy groceries|False|High
Write report|True|Medium
```

This file is automatically created and updated.

---

## 📁 Project Structure

```
todo-cli-python/
├── todo_cli.py
├── tasks.txt
└── README.md
```

---

## 👨‍💻 Author

Chathil Rajarathna
