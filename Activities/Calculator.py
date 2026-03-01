def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b): return a / b
def mod(a, b): return a % b

while True:
    try:
        print("\nPYTHON CALCULATOR\n")
        
        operation = float(input("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus \nPlease type the number of the selected operation: "))
        if operation > 5 or operation < 1:
            print("\nInvalid input please select only from 1 to 5\n")
            continue
        
        a = float(input("Enter your first number: "))
        b = float(input("Enter your seconde number: "))
        
        if (operation == 1):
            print(f"Addition Result: {add(a, b)}")
        elif (operation == 2):
            print(f"Subtraction Result: {sub(a, b)}")
        elif (operation == 3):
            print(f"Multiplication Result: {mult(a, b)}")
        elif (operation == 4):
            print(f"Division Result: {div(a, b)}")
        elif (operation == 5):
            print(f"Modulus Result: {mod(a, b)}")
        else:
            break
    except ValueError:
        print("NUMBER NGA LANG DEBAAA")