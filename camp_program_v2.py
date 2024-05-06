""" Program for Tane's 'Living Springs Holiday Camps'. The program will enable students to register themselves for the camp of their choice and record their details.

v2 - getChoice(): Displays camp choices and their durations, prices, and difficulties. Function asks for the user the input the student's camp of choice and saves the input. Camp choice is saved into the program
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
        
def welcome():
    print("\n= = = = = = = = = = Living Springs Camps - Registration = = = = = = = = = =\n")
    
    start = str(input("Would you like to register a student? (Y/N): "))
    
    if start.capitalize() == 'Yes' or start.capitalize() == 'Y':
        # If the user inputs 'yes', then the program goes ahead to ask for the user's information.
        name = str(input("Please enter the student's name: "))
        age = int(input("Please enter the student's age in years: ")) 
        print()
    
    