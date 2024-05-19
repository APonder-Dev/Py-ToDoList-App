"""
Created By Anthony -- 5/19/2024 
https://github.com/Wazupbutrcup

This application will allow you to add tasks, remove tasks, and mark tasks as complete.
"""

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Removed task: "{removed_task["task"]}"')
        else:
            print("Invalid task number")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f'Marked task "{self.tasks[task_number]["task"]}" as complete')
        else:
            print("Invalid task number")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Complete" if task["completed"] else "Incomplete"
                print(f'{i + 1}. {task["task"]} - {status}')

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            todo_list.complete_task(task_number)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
