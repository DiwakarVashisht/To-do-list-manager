class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task deleted:", task)
        else:
            print("Task not found:", task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_manager = ToDoListManager()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_manager.add_task(task)
        elif choice == "2":
            task = input("Enter task to delete: ")
            todo_manager.delete_task(task)
        elif choice == "3":
            todo_manager.display_tasks()
        elif choice == "4":
            print("Exiting..")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
