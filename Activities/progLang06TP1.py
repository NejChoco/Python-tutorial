def get_positive_input(prompt):
    value = float(input(prompt))
    if value < 0:
        raise ValueError("Negative numbers are not allowed.")
    return value

def calculate_total_cost(venue, catering, decorations, entertainment, miscellaneous):
    total_cost = 0
    total_cost += venue
    total_cost += catering
    total_cost += decorations
    total_cost += entertainment
    total_cost += miscellaneous
    return total_cost

def check_budget(total_cost, predefined_budget):
    if total_cost > predefined_budget:
        return "Budget Exceeded"
    elif total_cost < predefined_budget:
        return "Budget Not Exceeded"
    else:
        return "Budget Exactly Matched"

while True:
    try:
        print("\nBUDGET PLAN\n")
        print("====================================================")
        predefined_budget = get_positive_input("Predefined budget: ")
        print("====================================================")
        venue = get_positive_input("Venue: ")
        catering = get_positive_input("Catering: ")
        decoration = get_positive_input("Decorations: ")
        entertainment = get_positive_input("Entertainment: ")
        miscellaneous = get_positive_input("Miscellaneous: ")

        total_cost = calculate_total_cost(venue, catering, decoration, entertainment, miscellaneous)

        print("====================================================")
        print(f"Predefined Budget: {predefined_budget} \nTotal Cost: {total_cost}")
        print(f"Budget Verdict: {check_budget(total_cost, predefined_budget)}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter positive numerical numbers only.")
        continue
    print("====================================================")
    press = input("Continue? \nPress any key to continue \nOr press N to Cancel\n")
    if press.strip().upper() == 'N':
        print("====================================================")
        print("Thank you for using the budget plan")
        break
    print("====================================================")