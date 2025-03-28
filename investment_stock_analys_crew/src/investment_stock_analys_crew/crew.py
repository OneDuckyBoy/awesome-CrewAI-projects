from typing import List
from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
from crewai_tools import SerperDevTool,MDXSearchTool,FileReadTool # type: ignore
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource # type: ignore


import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

os.environ["SERPER_API_KEY"] =os.getenv("SERPER_API_KEY")


@CrewBase
class InvestmentStockAnalysCrew:

    def __init__(self, stock_1,stock_2):
        self.stock_1,self.stock_2 = stock_1,stock_2


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def web_research_agent(self) -> Agent:
        search_tool = SerperDevTool()

        return Agent(
            config=self.agents_config['web_research_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            output= f"results/{self.stock_1} {self.stock_2}.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file = f"results/{self.stock_1} {self.stock_2}.md"

        )

    @agent
    def stock_report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_report_writer_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='research/'+self.stock_1+" "+self.stock_2+'.md'),
                MDXSearchTool(mdx='research/'+self.stock_1+" "+self.stock_2+'.md')
            ]
        )
    @task
    def stock_report_writer_task(self)-> Task:
        return Task(
            config=self.tasks_config['stock_report_writer_task'],
            agent=self.stock_report_writer_agent(),
            allow_delegation=False,
            tools=[
                FileReadTool(file_path='research/'+self.stock_1+" "+self.stock_2+'.md'),
                MDXSearchTool(mdx='research/'+self.stock_1+" "+self.stock_2+'.md')
            ],
        )
    @agent
    def qa_stock_report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_stock_report_agent'],
            allow_delegation=True,
            verbose=True,
            output_file = f"results/{self.stock_1} {self.stock_2}.md"

        )
    @task
    def qa_stock_report_task(self) -> Task:
        task = Task(
            config=self.tasks_config['qa_stock_report_task'],
            agent=self.qa_stock_report_agent(),
            output_file = f"results/{self.stock_1} {self.stock_2}.md"

        )
    

        return task


    
    @crew
    def crew(self) -> Crew:
        example_articles = [
    TextFileKnowledgeSource(file_path="example_analys_1.md"),
    TextFileKnowledgeSource(file_path="example_analys_2.md"),
]
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
            knowledge_sources=example_articles,
        )