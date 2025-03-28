import sys
from lawyer_agent_crew.crew import LegalAgentCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Legal Agent Crew")
    print('-------------------------------')

    legal_problem = "My Boss didn't pay me my salary for the last 3 months " \
    "and when I ask him about it he always says he will pay it later" # this is an example legal problem -
                                                                      # I don't have that problem - saying it just in case
    personal_information = "I am Caucasian male, 27 years old, I live in Westside Los Angeles, California " \
    "and I work as a Project manager at a large Company" # fake address and job, of course
    inputs = {
        "legal_problem":legal_problem,
        "personal_information":personal_information,
    }
   
    results= LegalAgentCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The educated legal answer is in the results folder")
    print("########################\n")
 


