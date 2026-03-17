def outer_function():
    z = 15 # Enclosing variable
    def inner_function():
        print(z) # Accessing the enclosing scope variable
    inner_function() # This will print 15
outer_function()