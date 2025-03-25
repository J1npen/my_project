names = ["jinpen", "zhangsan", "lisi", "wangwu"]
print(names)
print(names[0])

# Access the last element in the list
print(names[-1])

# Append an element to the end of the list
names.append("zhaoliu")
print(names)

# Insert an element at a specific position
names.insert(2, "sunqi")
print(names)

# Remove an element from the list
names.remove("sunqi")
print(names)

# Removing an Item Using the del Statement
del names[2]
print(names)

# Removing an Item Using the pop() Method
popped_name = names.pop()
print(names)
print(popped_name)