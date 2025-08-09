#Operators

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = tip_percent * meal_cost / 100
    tax = tax_percent * meal_cost / 100
    
    print(round(meal_cost + tip + tax));
