# Day 6 Project: To Do List Manager

from datetime import datetime

# represents a single to do task
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
    
    
    def mark_complete(self):
        self.completed = True
    
    
    def update(self, title=None, description=None):
        if title:
            self.title = title
        if description:
            self.description = description
    
    
    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"[{status}] {self.title} - {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})")

# TodoList class manages multiple Task objects
class TodoList:
    def __init__(self):
        self.tasks = []

    # Add a new task
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully!")

    # Remove a task by title
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed successfully!")
                return
        print(f"Task '{title}' not found!")

    # Update a task by title
    def update_task(self, title):
        for task in self.tasks:
            if task.title == title:
                new_title = input("Enter new title (leave blank to keep same): ").strip()
                new_desc = input("Enter new description (leave blank to keep same): ").strip()
                task.update(new_title or None, new_desc or None)
                print(f"Task '{title}' updated successfully!")
                return
        print(f"Task '{title}' not found!")

    # Mark a task as complete by title
    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete!")
                return
        print(f"Task '{title}' not found!")

    # Display all tasks
    def show_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour Tasks:")
        for task in self.tasks:
            if show_completed or not task.completed:
                task.display()


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
            title = input("Enter task title to remove: ").strip()
            todo_list.remove_task(title)
        elif choice == "3":
            title = input("Enter task title to update: ").strip()
            todo_list.update_task(title)
        elif choice == "4":
            title = input("Enter task title to mark complete: ").strip()
            todo_list.complete_task(title)
        elif choice == "5":
            todo_list.show_tasks(show_completed=True)
        elif choice == "6":
            todo_list.show_tasks(show_completed=False)
        elif choice == "7":
            print("Keep your tasks organized")
            break
        else:
            print("Invalid choice. Try again.")


main()
