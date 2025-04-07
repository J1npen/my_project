import json

class json_file:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_json()

    def load_json(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty dictionary.")
            return {}

    def save_json(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_entry(self, key, value):
        self.data[key] = value
        self.save_json()

    def remove_entry(self, key):
        if key in self.data:
            del self.data[key]
            self.save_json()
        else:
            print(f"Key '{key}' not found.")

    def get_entry(self, key):
        return self.data.get(key, None)

    def display_data(self):
        print(json.dumps(self.data, indent=4))