import sys
from subject_teaching_crew.crew import SubjectTeachingCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Subject Teaching Crew")
    print('-------------------------------')

    subject = "3D printing and 3d modeling"
    level_of_knowledge = "from beginer to advanced" # "normal"
    inputs = {
        "subject":subject,
        "level_of_knowledge": level_of_knowledge
        
    }
    results= SubjectTeachingCrew(subject).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Lesson material is in the results folder")
    print("########################\n")
 


