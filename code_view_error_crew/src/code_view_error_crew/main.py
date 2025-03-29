import sys
from code_view_error_crew.crew import SolveCodeErrorFromImageCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Solve Code Error From Image Crew")
    print('-------------------------------')


    inputs = {
        
    }
    results= SolveCodeErrorFromImageCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The solution is in the results folder")
    print("########################\n")
 


