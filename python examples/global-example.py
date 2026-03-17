x = 10
def modify_global():
    global x
 # Declare that we are modifying the global variable 'x'
x = 20
modify_global()
print(x) # Prints 20