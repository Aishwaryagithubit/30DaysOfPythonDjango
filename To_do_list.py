import json
import uuid
from datetime import datetime

DATA_FILE = "tasks.json"

# Task class
class Task:
    def __init__(self, title, description=""):
        self.id = str(uuid.uuid4())  # unique id
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_complete(self):
        self.completed = True

    def update(self, title=None, description=None):
        if title:
            self.title = title
        if description:
            self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'])
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        return task

# TodoList class
class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    # Load tasks from JSON
    def load_tasks(self):
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                return [Task.from_dict(t) for t in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Data file corrupted, starting fresh.")
            return []

    # Save tasks to JSON
    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    # Helper
    def find_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task.title}' added successfully!")

    def remove_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task '{task.title}' removed successfully!")
        else:
            print("Task not found!")

    def update_task(self, task_id, title=None, description=None):
        task = self.find_task(task_id)
        if task:
            task.update(title, description)
            self.save_tasks()
            print(f"Task '{task.title}' updated successfully!")
        else:
            print("Task not found!")

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.mark_complete()
            self.save_tasks()
            print(f"Task '{task.title}' marked as complete!")
        else:
            print("Task not found!")

    def show_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour Tasks:")
        for t in self.tasks:
            if show_completed or not t.completed:
                status = "Completed" if t.completed else "Pending"
                print(f"[{status}] {t.title} - {t.description} (ID: {t.id}, Created: {t.created_at})")

# Main program
def main():
    todo_list = TodoList()
    print("Welcome to To-Do List Manager")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Mark Task Complete")
        print("5. Show All Tasks")
        print("6. Show Pending Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":

            title = input("Enter task title: ").strip()
            desc = input("Enter task description (optional): ").strip()
            task = Task(title, desc)
            todo_list.add_task(task)

        elif choice == "2":

            task_id = input("Enter task ID to remove: ").strip()
            todo_list.remove_task(task_id)

        elif choice == "3":
            task_id = input("Enter task ID to update: ").strip()
            new_title = input("Enter new title (leave blank to keep same): ").strip() 
            new_desc = input("Enter new description (leave blank to keep same): ").strip()
            todo_list.update_task(task_id, new_title, new_desc)

        elif choice == "4":
            task_id = input("Enter task ID to mark complete: ").strip()
            todo_list.complete_task(task_id)

        elif choice == "5":
            todo_list.show_tasks(show_completed=True)

        elif choice == "6":
            todo_list.show_tasks(show_completed=False)

        elif choice == "7":
            print("Keep your tasks organized")
            break
        else:
            print("Invalid choice.Try again.")

main()
