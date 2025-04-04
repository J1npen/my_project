def load_categories(filename="categories.txt"):
    """
    Load categories from a file.
    Each category should be on a new line.
    :param filename: The name of the file containing categories.
    :return: A list of categories.
    """
    try:
        with open(filename, "r") as file:
            categories = [line.strip() for line in file.readlines() if line.strip()]
        return categories
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    
def add_category(category, filename="categories.txt"):
    """
    Add a new category to the categories file.
    :param category: The category to add.
    :param filename: The name of the file to save the category.
    """    
    with open(filename, "a") as file:
        file.write(category + "\n")
    print(f"Category '{category}' added.")

def remove_category(category, filename="categories.txt"):
    """
    Remove a category from the categories file.
    :param category: The category to remove.
    :param filename: The name of the file to save the category.
    """
    categories = load_categories(filename)
    if category in categories:
        categories.remove(category)
        with open(filename, "w") as file:
            for cat in categories:
                file.write(cat + "\n")
        print(f"Category '{category}' removed.")
    else:
        print(f"Category '{category}' not found.")

def list_categories(filename="categories.txt"):
    """
    List all categories from the categories file.
    :param filename: The name of the file containing categories.
    """
    categories = load_categories(filename)
    if categories:
        print("Categories:")
        for category in categories:
            print(f"- {category}")
    else:
        print("No categories found.")

def interate_with_categories():
    """
    Interact with categories: add, remove, or list categories.
    """
    while True:
        command = input("\nEnter a command (add/remove/list/quit): ").strip().lower()
        
        if command == "add":
            category = input("Enter a new category: ").strip()
            add_category(category)
        
        elif command == "remove":
            list_categories()
            if not load_categories():
                print("No categories to remove.")
                continue
            category = input("Enter the category to remove: ").strip()
            remove_category(category)
        
        elif command == "list":
            list_categories()
        
        elif command == "quit":
            print("Goodbye!")
            break
        
        else:
            print("Unknown command.")