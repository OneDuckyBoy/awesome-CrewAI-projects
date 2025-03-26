import sys
import yaml
from marketing_posts_crew.crew import MarketingPostsCrew
from crewai_tools import FileWriterTool,FileReadTool

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Health and Fittness planner Crew")
    print('-------------------------------')

    person_info = "make a health and fittness plan for a male, 27 years old. He is tall around 5.6~5.7 feet tall (around 165 sm). " \
    "He doesn't train very much, but is willing to strart going to the gym to gain muscle and lose fat. He is around 180 pounds. " \
    "Can you also make a food and nutrition plan."
    main_topic = "health and fittness plan"
    inputs = {
        "person_info":person_info,
        "main_topic":main_topic
    }
    test= MarketingPostsCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Here is the plan")
    print("########################\n")
    print("it is also saved in the results folder")
    print(test)
    with open(f"results/{main_topic}.txt", "w") as file:
        file.write(test.raw)
   



