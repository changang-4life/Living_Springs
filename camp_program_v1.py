""" Program for Tane's 'Living Springs Holiday Camps'. The program will enable students to register themselves for the camp of their choice and record their details.

v1 - main(): Asks if they want to register a student, then asks for their name and age if they input 'yes'. Name and age is saved into the program
"""
total_cost = 0

WSPRICE = 800 # Price for 'Walking and Social Skills' camp option
KSPRICE = 400 # Price for 'Kayaks and Swimming' camp option
TBPRICE = 900 # Price for 'Tramping and Biking' camp option

STLPRICE = 80 # Price for shuttle transportation option

def welcome():
    print("\n= = = = = = = = = = Living Springs Camps - Registration = = = = = = = = = =\n")
    
    start = str(input("Would you like to register a student? (Y/N): "))
    
    if start.capitalize() == 'Yes' or start.capitalize() == 'Y':
        # If the user inputs 'yes', then the program goes ahead to ask for the user's information.
        name = str(input("Please enter the student's name: "))
        age = int(input("Please enter the student's age in years: ")) 
        print()
        return name, age
        