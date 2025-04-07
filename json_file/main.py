import module.greet_user as gu
import module.interative_json_file as ijf

data_file = ijf.json_file("data.json")

gu.greet_user()

while True:
    command = input("Enter a command (add, remove, get, display, exit): ").strip().lower()
    if command == "add":
        key = input("Enter the key: ").strip()
        value = input("Enter the value: ").strip()
        data_file.add_entry(key, value)
    elif command == "remove":
        key = input("Enter the key to remove: ").strip()
        data_file.remove_entry(key)
    elif command == "get":
        key = input("Enter the key to get: ").strip()
        value = data_file.get_entry(key)
        print(f"Value for '{key}': {value}")
    elif command == "display":
        data_file.display_data()
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")