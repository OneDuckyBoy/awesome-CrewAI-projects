import sys
from competitor_analys_crew.crew import CompetitorAnalysCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Competitor Analys Crew")
    print('-------------------------------')

    company_name = "Dreamix"
    
    inputs = {
        "company_name":company_name,
        
    }
   
    results= CompetitorAnalysCrew(company_name).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The analys is in the results folder")
    print("########################\n")
 


