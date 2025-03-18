'''
This is the main program to start the execution of the code
'''

# Imports of Custom Function
from home import *
from custom_functions import *


# Calling my custom function to display a welcome message
print_welcome()


# Write code for user interaction here
user_input_track = ""
lenuserinput = (len(user_input_track))

'''
The code segment asks the user what major they would like to study in college if they have not entered anything yet.
Based on what number they enter (1 or 2), the program will then give the user a list of opportunities for the selected 
track. If the user selects 3, the program will exit. 
'''

while True:
    if lenuserinput == 0:
        user_input_track = input("Please enter what major you would like to study in college (1: Pre-Med, 2: Engineering, 3:Exit): ")
        lenuserinput += 1
    print(f"You selected {user_input_track}")
    user_input_opportunities = ""
    if user_input_track == "1":
        user_input_opportunities = input("Please select one of the following that you would like to see for the Pre-Med track:\n1: Internship\n2: Volunteering\n3: Research\n4: Colleges\n5: Professions\n")
        user_input_opportunities = prompt_pre_med_opportunities(user_input_opportunities)

    elif user_input_track == "2":
        user_input_opportunities = input("Please select one of the following that you would like to see for the Engineering track:\n1: Internship\n2: Volunteering\n3: Research\n4: Colleges\n5: Professions\n")
        prompt_eng_opportunities(user_input_opportunities)

    elif user_input_track == "3":
        print("Have a nice day")
        break




    user_continue = input("Would you like to keep looking at the current major or choose another one? (1: Keep Looking:, 2: Choose another, 3: Exit) : ")

    if user_continue == "1":
        break
    elif user_continue == "2":
        user_input_track = ""
        lenuserinput = 0
    elif user_continue == "3":
        print("Have a nice day")
        break
    else:
        print("Invalid input. Please select a valid option.")
'''
This feature increases user compatibility by allowing the user to keep searching for different opportunities in the same 
previously selected major instead of having to select the major again. It also allows the user to
choose another major to explore or to exit the program
'''



