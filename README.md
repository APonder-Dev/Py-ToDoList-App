# ✅ To-Do List Application

A simple command-line based to-do list app written in Python. Easily add, remove, complete, and view tasks with a clean and intuitive interface — perfect for managing your daily checklist!

---

## ✨ Features

- ➕ **Add Task** – Add new tasks to your to-do list
- ❌ **Remove Task** – Delete tasks by number
- ✅ **Complete Task** – Mark tasks as complete
- 📋 **Show Tasks** – Display tasks with their status
- 🚪 **Exit** – Close the application

---

## 💻 Requirements

- Python 3.x (Download: [python.org](https://www.python.org))

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app
```

---

## 🚀 Usage

```bash
python todolist.py
```

Then use the menu:

- 1: Add Task
- 2: Remove Task
- 3: Complete Task
- 4: Show Tasks
- 5: Exit

---

## 🧪 Example Session

```plaintext
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 1
Enter a new task: Buy groceries
Added task: "Buy groceries"

Choose an option: 4
1. Buy groceries - Incomplete

Choose an option: 3
Enter the task number: 1
Marked task "Buy groceries" as complete

Choose an option: 4
1. Buy groceries - Complete
```

---

## 🧱 Code Structure

### `todo_list.py`

Main script with two components:

#### Class: `ToDoList`

- `tasks`: List of dictionaries with `"task"` and `"completed"` keys
- `add_task(task)`: Add new task
- `remove_task(index)`: Remove task by number
- `complete_task(index)`: Mark task as complete
- `show_tasks()`: Display all tasks

#### Function: `main()`

- Menu loop interface
- Handles user input
- Calls `ToDoList` methods accordingly

---

## 🤝 Contributing

We welcome contributions!

1. Fork this repository
2. Create a new branch:
```bash
git checkout -b feature-branch
```
3. Commit your changes:
```bash
git commit -m "Added a new feature"
```
4. Push to your branch:
```bash
git push origin feature-branch
```
5. Open a Pull Request

---

## 📝 License

Licensed under the **MIT License**.  
See the [`LICENSE`](LICENSE) file for full terms.

---

## 📬 Contact

For any inquiries or feedback, reach out to [aponder.dev](mailto:aponder.dev)

---

Thanks for staying productive with the **To-Do List App**! 🧠✅
