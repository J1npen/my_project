# to_do_list.py

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
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks("todo.txt")
    if not tasks:
        print("No tasks found.")
    
    while True:
        command = input("\nEnter a command (add/show/remove/quit): ").strip().lower()

        if command == "add":
            task = input("Enter a new task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        
        elif command == "show":
            show_tasks(tasks)
        
        elif command == "remove":
            show_tasks(tasks)
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif command == "quit":
            print("Goodbye!")
            break
        
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
