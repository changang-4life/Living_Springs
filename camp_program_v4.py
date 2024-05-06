""" Program for Tane's 'Living Springs Holiday Camps'. The program will enable students to register themselves for the camp of their choice and record their details.

v4 - mealChoice(): Meal choices are displayed and the program asks which meal type they would like.
"""
total_cost = 0

WSPRICE = 800 # Price for 'Walking and Social Skills' camp option
KSPRICE = 400 # Price for 'Kayaks and Swimming' camp option
TBPRICE = 900 # Price for 'Tramping and Biking' camp option

STLPRICE = 80 # Price for shuttle transportation option

def getChoice():
        print("Activities and Costs:\n\
          1. Easy ~ Walking and Social Skills (5 Days) -- $800\n\
          2. Moderate ~ Kayaks and Swimming (3 Days) -- $400\n\
          3. Difficult ~ Tramping and Biking (4 Days) -- $900\n")
        
        choice = int(input("Please enter your camp of choice with its corresponding number above: "))
        return choice
    
def shuttleChoice():
    shuttle_choice = str(input("Would you like to pay an extra $80 for shuttle transport? (Y / N): "))
    return shuttle_choice
    
def mealChoice():
    print("Meal Choices:\n\
        1. standard\n\
        2. vegetarian\n\
        3. vegan")
    
    meal_choice = int(input(f"Please enter {name}'s meal choice with its corresponding number above: "))
    return meal_choice

def welcome():
    print("\n= = = = = = = = = = Living Springs Camps - Registration = = = = = = = = = =\n")
    
    start = str(input("Would you like to register a student? (Y/N): "))
    
    if start.capitalize() == 'Yes' or start.capitalize() == 'Y':
        # If the user inputs 'yes', then the program goes ahead to ask for the user's information.
        name = str(input("Please enter the student's name: "))
        age = int(input(f"Please enter the {name}'s age in years: ")) 
        print()
        return name, age
        
