from module.todo_list import TodoList, interact_with_todo_list
from pathlib import Path

# 获取当前文件夹路径
current_dir = Path('.')

# 使用 glob 匹配 txt 文件
txt_files = list(current_dir.glob('*.txt'))

while True:
    # 打印结果
    print("Your to-do list files:")
    for file in txt_files:
        print(file.stem)

    prompt = "Enter the name of your to-do list, or type 'quit' to quit: "
    list_name = input(prompt).strip()
    if not list_name:
        list_name = "todo.txt"
    elif list_name.lower() == "quit":
        print("Goodbye!")
        break

    # Create a instance of TodoList
    todo_list = TodoList(list_name+".txt")

    # Use the interact_with_todo_list function to manage the todo list
    interact_with_todo_list(todo_list)