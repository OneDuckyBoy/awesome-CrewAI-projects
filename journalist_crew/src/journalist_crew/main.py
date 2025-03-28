import sys
from journalist_crew.crew import ArticleMakingCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Article making crew")
    print('-------------------------------')

    topic = "The art of Meditation"
    
    inputs = {
        "topic":topic,
        
    }
   
    results= ArticleMakingCrew(topic).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The finished article is in the results folder")
    print("########################\n")
 


