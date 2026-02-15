try: 
    user_input = int(input("Enter your age: "))
    if user_input < 0:
        raise ValueError("Age cannot be negative.")
    elif user_input < 13:
        print("You are categorized as: Child")
    elif user_input < 20:
        print("You are categorized as: Teenager")
    elif user_input < 30:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Trentahin na")
except ValueError:
    print("Number lang pwede deba!")