app = ['ChatGPT', 'YouTube', 'Instagram', 'Facebook', 'Twitter']
print('Original List:', app)

# sorted() function
# sorted() function is used to sort the list in ascending order.
# It returns a new sorted list but it does not change the original list.
sorted_app = sorted(app, reverse=True)
print('\nSorted List:', sorted_app)
print('Original List:', app)

# sort() method 
# sort() method is used to sort the list in ascending order.
# It does not return any value but it changes from the original list.
app.sort()
print('\nSorted List:', app)
print('Original List:', app)

# reverse() method
# reverse() method is used to reverse the list.
# It does not return any value but it changes from the original list.
app.reverse()
print('\nReversed List:', app)
print('Original List:', app)
