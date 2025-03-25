# a for loop example
game = ['Ready', 'Set', 'Go!']
for item in game:
    print(item)
# Output:
# Ready
# Set
# Go!
# The for loop iterates over the list game and prints each item in the list.
# The variable item is used to store the current item in the iteration.
# The loop continues until all items in the list have been printed.

# The for loop can also be used to iterate over a string:
for letter in 'Python':
    print(letter, end=' ')
# Output: P y t h o n
# The for loop iterates over the string 'Python' and prints each character in the string.

# The for loop can also be used to iterate over a range of numbers:
for number in range(1, 6):
    print(number, end=' ')
# Output: 1 2 3 4 5
# The for loop iterates over the range of numbers from 1 to 6 and prints each number in the range.

# The for loop can also be used to iterate over a dictionary:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key, value)
# Output:
# name John
# age 30
# city New York
# The for loop iterates over the dictionary person and prints each key-value pair in the dictionary.
# The variables key and value are used to store the key and value of each pair in the iteration.

# The for loop can also be used to iterate over a list of tuples:
people = [('John', 30), ('Jane', 25), ('Jake', 35)]
for name, age in people:
    print(name, age)
# Output:
# John 30
# Jane 25
# Jake 35
# The for loop iterates over the list of tuples people and prints each tuple in the list.
# The variables name and age are used to store the elements of each tuple in the iteration.

# The for loop can also be used to iterate over a list of lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for number in row:
        print(number, end=' ')
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
# The outer for loop iterates over the list of lists matrix and prints each list in the list.
# The inner for loop iterates over each list in the matrix and prints each number in the list.

# The for loop can also be used to iterate over a list of lists using list comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [number for row in matrix for number in row]
print(numbers) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# The list comprehension creates a new list numbers by iterating over the list of lists matrix and flattening it into a single list.

# The for loop can also be used to iterate over a list and modify its elements:
game = ['Ready', 'Set', 'Go!']
for i in range(len(game)):
    game[i] = game[i].lower()
print(game) # Output: ['ready', 'set', 'go!']
# The for loop iterates over the list game and modifies each item in the list to lowercase using the lower() method.

# The for loop can also be used to iterate over a list and remove elements from it:
game = ['Ready', 'Set', 'Go!']
for item in game[:]: # list slicing
    if item == 'Set':
        game.remove(item)
print(game) # Output: ['Ready', 'Go!']
# The for loop iterates over a copy of the list game using list slicing and removes the item 'Set' from the original list.

print(game) # Output: ['Ready', 'Go!']