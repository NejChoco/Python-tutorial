def my_function():
    y = 5 # Local variable
    print(y)
my_function() # This will print 5
print(y) # This will raise an error because 'y' is not accessible outside the function
