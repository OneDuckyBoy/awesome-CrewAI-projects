import sys
from investment_stock_analys_crew.crew import InvestmentStockAnalysCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Competitor Analys Crew")
    print('-------------------------------')

    stock_1 = "AMZN" # Amazon stock
    stock_2 = "META" # META stock
    
    inputs = {
        "stock_1":stock_1,
        "stock_2":stock_2,
        
    }
   
    results= InvestmentStockAnalysCrew(stock_1,stock_2).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The analys is in the results folder")
    print("########################\n")
 


