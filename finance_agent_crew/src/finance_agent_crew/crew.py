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
class FinanceAgentCrew:

    def __init__(self, current_financial_plan):
        self.current_financial_plan = current_financial_plan


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
            output= f"research/financial_plan_research.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file = f"research/financial_plan_research.md"

        )

    @agent
    def financial_plan_analys_report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_plan_analys_report_writer_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='research/financial_plan_research.md'),
                MDXSearchTool(mdx='research/financial_plan_research.md')
            ]
        )
    @task
    def financial_plan_analys_report_writer_task(self)-> Task:
        return Task(
            config=self.tasks_config['financial_plan_analys_report_writer_task'],
            agent=self.financial_plan_analys_report_writer_agent(),
            allow_delegation=False,
            tools=[
                FileReadTool(file_path='research/'+self.current_financial_plan+'.md'),
                MDXSearchTool(mdx='research/financial_plan_research.md')
            ],
        )
    @agent
    def qa_report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_report_agent'],
            allow_delegation=True,
            verbose=True,
            output_file = f"results/new_financial_plan.md"

        )
    @task
    def qa_report_task(self) -> Task:
        task = Task(
            config=self.tasks_config['qa_report_task'],
            agent=self.qa_report_agent(),
            output_file = f"results/new_financial_plan.md"

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