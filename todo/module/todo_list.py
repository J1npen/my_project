def load_tasks(FILENAME):
    """Load tasks from a file."""
    try:
        with open(FILENAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, FILENAME="todo.txt"):
    """Save tasks to a file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display the tasks."""
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Create a function to add/show/remove/quit a todo
def interact_with_todo_list(todo_list):
    while True:
        command = input("\nEnter a command (add/show/remove/quit): ").strip().lower()

        if command == "add":
            task = input("Enter a new task: ").strip()
            todo_list.add_todo(task)
            print("Task added.")
        
        elif command == "show":
            todos = todo_list.get_todos()
            if not todos:
                print("No tasks found.")
            else:
                print("\nYour To-Do List:")
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
        
        elif command == "remove":
            todos = todo_list.get_todos()
            if not todos:
                print("No tasks to remove.")
                continue
            
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
            
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos[index]
                    todo_list.remove_todo(removed)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif command == "quit":
            print("Goodbye!\n")
            break
        
        else:
            print("Unknown command.")

# Creat a class TodoList
class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = load_tasks(self.filename)

    def add_todo(self, task):
        self.tasks.append(task)
        save_tasks(self.tasks, self.filename)

    def remove_todo(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            save_tasks(self.tasks, self.filename)
        else:
            print("Task not found.")

    def get_todos(self):
        return self.tasks