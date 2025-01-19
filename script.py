
from home import *
from custom_functions import *



print_welcome()


selected_food_type = ""

# Write code for user interaction here
user_input_track = ""
lenuserinput = (len(user_input_track))

while lenuserinput == 0:
    user_input_track = input("Please enter what major you would like to study in college (1: Pre-Med, 2: Engineering, 3:Exit): ")

    print(f"You selected {user_input_track}")
    user_input_opportunities = ""
    if user_input_track == "1":
        user_input_opportunities = input("Please select one of the following that you would like to see for the Pre-Med track:\n1: Internship\n2: Volunteering\n3: Research\n4: Colleges\n5: Professions\n6: Clubs\n")
        user_input_opportunities = prompt_pre_med_opportunities(user_input_opportunities)

    elif user_input_track == "2":
        user_input_opportunities = input("Please select one of the following that you would like to see for the Engineering track:\n1: Internship\n2: Volunteering\n3: Research\n4: Colleges\n5: Professions\n6: Clubs\n")
        prompt_eng_opportunities(user_input_opportunities)
    elif user_input_track == "3":
        print("Have a nice day")
        break




