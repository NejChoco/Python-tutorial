# Implicit variable declaration and binding
# The variable 'y' is implicitly declared and bound to an integer
y = 42
print(f"y is implicitly bound to {y} and its type is {type(y)}")
# The same variable 'y' is now implicitly bound to a string
y = "Python programming"
print(f"y is now implicitly bound to '{y}' and its type is {type(y)}")
# Now, 'y' is implicitly bound to a float
y = 3.14159
print(f"y is now implicitly bound to {y} and its type is {type(y)}")

# Finally, 'y' is implicitly bound to a list
y = [1, 2, 3, 4]
print(f"y is now implicitly bound to {y} and its type is {type(y)}")