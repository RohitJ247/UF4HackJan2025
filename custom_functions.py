#Imports independent static data (volunteering, internships, and research) from engineering_data and premed-data
from engineering_data import *
from premed_data import *

'''
This function provides the user with all of the information related to what number they input. This function only runs
if the user previously selected that they were interested in the engineering track. 
@param user_input_opportunities: If the user inputs: 
1: Lists all the available internships; 
2: Volunteering opportunities;
3: Research opportunities;
4: Best colleges for engineering;
5: Best professions for engineering;
'''
#This is for engineering data
def prompt_eng_opportunities(user_input_opportunities):

    if user_input_opportunities == "1":
        print("Here are all the internships available for your track")
        for i in einternships:
            print(i)

    elif user_input_opportunities == "2":
        print("Here are all the volunteering opportunities available for your track")
        for i in evolunteering:
            print(i)
    elif user_input_opportunities == "3":
        print("Here are all the research opportunities available for your track")
        for i in eresearch:
            print(i)
    elif user_input_opportunities == "4":
        print("Here are the best colleges for your coveted major")
        for i in ecollege:
            print(i)
    elif user_input_opportunities == "5":
        print("Here are the best professions suited for your major")
        for i in eprofession:
            print(i)
    return user_input_opportunities


'''
This function provides the user with all of the information related to what number they input. This function only runs
if the user previously selected that they were interested in the pre-med track. 
@param user_input_opportunities: If the user inputs: 
1: Lists all the available internships; 
2: Volunteering opportunities;
3: Research opportunities;
4: Best colleges for pre-med;
5: Best professions inthe medical field;
'''
def prompt_pre_med_opportunities(user_input_opportunities):

    if user_input_opportunities == "1":
        print("Here are all the internships available for your track")
        for i in pinternships:
            print(i)
    elif user_input_opportunities == "2":
        print("Here are all the volunteering opportunities available for your track")
        for i in pvolunteering:
            print(i)
    elif user_input_opportunities == "3":
        print("Here are all the research opportunities available for your track")
        for i in presearch:
            print(i)
    elif user_input_opportunities == "4":
        print("Here are the best colleges for your coveted major")
        for i in pcollege:
            print(i)
    elif user_input_opportunities == "5":
        print("Here are the best professions suited for your major")
        for i in pprofession:
            print(i)
    return user_input_opportunities