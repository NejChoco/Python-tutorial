"""

print("====================================================")
predefined_budget = float(input("predefined budget: ")) 
print("====================================================")
venue = float(input("venue: "))
catering = float(input("catering: "))
decoration = float(input("decoration: "))
entertainment=float(input("entertainment: "))
miscellaneous=float(input("miscellaneous: "))
print("====================================================")

def calculate_total_cost(venue, catering, decoration, entertainment, miscellaneous):
    return venue + catering + decoration + entertainment + miscellaneous

total_cost = calculate_total_cost(venue, catering, decoration, entertainment, miscellaneous)    

def check_budget(total_cost, predefined_budget):
    if total_cost > predefined_budget:
        return "Budget Exceeded"
    elif total_cost < predefined_budget:
        return "Budget Not Exceeded"
    else:
        return "Budget Exactly Matched"


print(f"Predefined Budget: {predefined_budget} \nTotal Cost: {total_cost}")
print(f"Budget Verdict: {check_budget(total_cost, predefined_budget)}")
"""
def calculate_total_cost(venue, catering, decoration, entertainment, miscellaneous):
    return venue + catering + decoration + entertainment + miscellaneous

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
        predefined_budget = float(input("predefined budget: ")) 
        print("====================================================")
        venue = float(input("venue: "))
        catering = float(input("catering: "))
        decoration = float(input("decoration: "))
        entertainment=float(input("entertainment: "))
        miscellaneous=float(input("miscellaneous: "))
        
        
        total_cost = calculate_total_cost(venue, catering, decoration, entertainment, miscellaneous) 
        
        print("====================================================")
        print(f"Predefined Budget: {predefined_budget} \nTotal Cost: {total_cost}")
        print(f"Budget Verdict: {check_budget(total_cost, predefined_budget)}")
    except ValueError:
        print("NUMBER NGA LANG DEBAAA")
        