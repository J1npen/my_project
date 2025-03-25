# Description: List comprehension examples
# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

# List comprehension with condition
even_squares = [n * n for n in numbers if n % 2 == 0]
print(even_squares)

# List comprehension with nested loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

# List comprehension with nested loop and condition
even = [x for row in matrix for x in row if x % 2 == 0]
print(even)

# List comprehension with nested loop and condition
even = [[x for x in row if x % 2 == 0] for row in matrix]
print(even)
    