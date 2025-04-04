# to_do_list.py

FILENAME = "todo.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    
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
