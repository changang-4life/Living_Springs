""" Program for Tane's 'Living Springs Holiday Camps'. The program will enable students to register themselves for the camp of their choice and record their details.

v5 - confirm(): Displays all the information thats been input for the student's registration and asks the user to confirm
"""
total_cost = 0

WSPRICE = 800 # Price for 'Walking and Social Skills' camp option
KSPRICE = 400 # Price for 'Kayaks and Swimming' camp option
TBPRICE = 900 # Price for 'Tramping and Biking' camp option

STLPRICE = 80 # Price for shuttle transportation option

def confirm():
    if shuttle_choice.capitalize() == 'Y' or shuttle_choice.capitalize() == 'Yes':
        print(f"Confirm that {name}, aged {age}, is registering for the {camp_choice} camp option over {length} days at a cost of {total_cost} plus $80 for shuttle transport? (Y / N): ")
        
    elif shuttle_choice.capitalize() == 'N' or shuttle_choice.capitalize() == 'No':
        print(f"Confrim that {name}, aged {age}, is registering for the {camp_choice} camp option over {length} days at a cost of {total_cost}? (Y / N): ")

def getChoice():
        print("Activities and Costs:\n\
          1. Easy ~ Walking and Social Skills (5 Days) -- $800\n\
          2. Moderate ~ Kayaks and Swimming (3 Days) -- $400\n\
          3. Difficult ~ Tramping and Biking (4 Days) -- $900\n")
        
        camp_choice = int(input("Please enter your camp of choice with its corresponding number above: "))
        return camp_choice
    
def shuttleChoice():
    shuttle_choice = str(input("Would you like to pay an extra $80 for shuttle transport? (Y / N): "))
    return shuttle_choice
    
def mealChoice():
    print("Meal Choices:\n\
        1. standard\n\
        2. vegetarian\n\
        3. vegan")
    
    meal_choice = int(input(f"Please enter {name.capitalize()}'s meal choice with its corresponding number above: "))
    return meal_choice

def welcome():
    print("\n= = = = = = = = = = Living Springs Camps - Registration = = = = = = = = = =\n")
    
    start = str(input("Would you like to register a student? (Y/N): "))
    
    if start.capitalize() == 'Yes' or start.capitalize() == 'Y':
        # If the user inputs 'yes', then the program goes ahead to ask for the user's information.
        name = str(input("Please enter the student's name: "))
        age = int(input(f"Please enter the {name.capitalize()}'s age in years: ")) 
        print()
        return name, age

    
    

    
