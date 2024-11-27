class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                print(f"{idx}. {task['task']} [{status}]")

    def add_task(self):
        """Add a new task to the list."""
        task_name = input("Enter the task name: ").strip()
        if task_name:
            self.tasks.append({'task': task_name, 'completed': False})
            print(f"Task '{task_name}' has been added.")
        else:
            print("Task name cannot be empty.")

    def mark_task_completed(self):
        """Mark a task as completed."""
        self.display_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1]['completed'] = True
                print(f"Task {task_number} has been marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        """Delete a task from the list."""
        self.display_tasks()
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        """Main method to run the application."""
        while True:
            print("\nTo-Do List Menu:")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Mark a task as completed")
            print("4. Delete a task")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self.display_tasks()
                elif choice == 2:
                    self.add_task()
                elif choice == 3:
                    self.mark_task_completed()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    print("Exiting the To-Do List application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select from the menu options.")
            except ValueError:
                print("Please enter a valid number.")

# Run the To-Do List application
if __name__ == "__main__":
    app = ToDoList()
    app.run()
