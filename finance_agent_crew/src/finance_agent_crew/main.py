import sys
from finance_agent_crew.crew import FinanceAgentCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Competitor Analys Crew")
    print('-------------------------------')
    current_financial_plan ="" 

    with open('info/current_financial_plan.md', 'r') as file:
        current_financial_plan = file.read()  # Read the entire content
        # print(current_financial_plan)
    
    
    
    inputs = {
        "current_financial_plan":current_financial_plan,
        
    }
   
    results= FinanceAgentCrew(current_financial_plan).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The corrected financial plan is in the results folder")
    print("########################\n")
 


