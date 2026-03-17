x = 100
 # Global variable
def my_function():
    x = 50 # Local variable, shadows the global variable
    print(x)
my_function() # Prints 50, because the local x shadows the global x
print(x) # Prints 100, the global x remains unchanged