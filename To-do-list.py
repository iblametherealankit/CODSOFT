import json
import os

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✖"
            print(f"{index}. {task['task']} [{status}]")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n--- To-Do List ---")
        todo_list.view_tasks()
        print("\nOptions: 1. Add 2. Complete 3. Delete 4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_num = int(input("Enter task number to complete: ")) - 1
            todo_list.mark_completed(task_num)
        elif choice == '3':
            task_num = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_num)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
