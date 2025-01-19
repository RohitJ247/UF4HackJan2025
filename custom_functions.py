

from engineering_data import *
from premed_data import *

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
    elif user_input_opportunities == "5":
        print("Here are the best professions suited for your major")
    elif user_input_opportunities == "6":
        print("Here are some clubs that you should join that can help you advance your skills in your desired major")
    return user_input_opportunities


#This is for pre_med data
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
    elif user_input_opportunities == "5":
        print("Here are the best professions suited for your major")
    elif user_input_opportunities == "6":
        print("Here are some clubs that you should join that can help you advance your skills in your desired major")
    return user_input_opportunities