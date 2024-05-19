# To-Do List Application

## Overview

This is a simple command-line based to-do list application written in Python. The application allows users to add tasks, remove tasks, and mark tasks as complete. It provides a user-friendly interface for managing daily tasks and keeping track of completed ones.

## Features

- **Add Task**: Add a new task to the to-do list.
- **Remove Task**: Remove an existing task from the list by its number.
- **Complete Task**: Mark a task as complete by its number.
- **Show Tasks**: Display all tasks with their completion status.
- **Exit**: Exit the application.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/todo-list-app.git
    cd todo-list-app
    ```

2. **Requirements**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Run the Application**:
    ```bash
    python todo_list.py
    ```

2. **Menu Options**:
    - **1. Add Task**: Prompts you to enter a new task.
    - **2. Remove Task**: Prompts you to enter the task number to remove.
    - **3. Complete Task**: Prompts you to enter the task number to mark as complete.
    - **4. Show Tasks**: Displays the list of tasks with their status.
    - **5. Exit**: Exits the application.

## Example

Here is an example interaction with the application:

```plaintext
To-Do List Application
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 1
Enter a new task: Buy groceries
Added task: "Buy groceries"

To-Do List Application
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 4
1. Buy groceries - Incomplete

To-Do List Application
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 3
Enter the task number to mark as complete: 1
Marked task "Buy groceries" as complete

To-Do List Application
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 4
1. Buy groceries - Complete
 
To-Do List Application
1. Add Task
2. Remove Task
3. Complete Task
4. Show Tasks
5. Exit
Choose an option: 5
Exiting the application.
```

## Code Structure

- **`todo_list.py`**: The main Python script containing the `ToDoList` class and the `main` function to run the application.

### Class: `ToDoList`

- **Attributes**:
  - `tasks`: A list to store tasks. Each task is represented as a dictionary with keys `"task"` and `"completed"`.

- **Methods**:
  - `add_task(task)`: Adds a new task to the list.
  - `remove_task(task_number)`: Removes a task by its index.
  - `complete_task(task_number)`: Marks a task as complete by its index.
  - `show_tasks()`: Displays all tasks with their status.

### Function: `main`

- Provides a menu-driven interface for the user to interact with the to-do list.
- Loops until the user decides to exit the application.
- Handles user input and calls the appropriate `ToDoList` methods based on the selected option.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. **Fork the Repository**
2. **Create a New Branch**
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit Your Changes**
    ```bash
    git commit -m "Description of your changes"
    ```
4. **Push to the Branch**
    ```bash
    git push origin feature-branch
    ```
5. **Open a Pull Request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue on the GitHub repository.

---

### Notes:
- Replace `your-username` in the clone URL with your actual GitHub username if you plan to host this on GitHub.
- Ensure that the file names (`ToDoList.py` and `ToDoList(GUI).py`) match the actual file names you have used in your project. If they are different, update the README accordingly.
- Include the `LICENSE` file in your repository if you choose to specify a license.