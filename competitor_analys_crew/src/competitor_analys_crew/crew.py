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
class CompetitorAnalysCrew:

    def __init__(self, company_name):
        self.company_name = company_name


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
            output=f"research/{self.company_name} competitors.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file = f"research/{self.company_name} competitors.md"

        )

    @agent
    def competitor_report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_report_writer_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='research/'+self.company_name+'.md'),
                MDXSearchTool(mdx='research/'+self.company_name+' competitors.md')
            ]
        )
    @task
    def competitor_report_writer_task(self)-> Task:
        return Task(
            config=self.tasks_config['competitor_report_writer_task'],
            agent=self.competitor_report_writer_agent(),
            allow_delegation=False,
            tools=[
                FileReadTool(file_path='research/'+self.company_name+' competitors.md'),
                MDXSearchTool(mdx='research/'+self.company_name+' competitors.md')
            ],
        )
    @agent
    def qa_competitor_report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_competitor_report_agent'],
            allow_delegation=True,
            verbose=True,
            output_file = f"results/{self.company_name} analys.md"

        )
    @task
    def qa_competitor_report_task(self) -> Task:
        task = Task(
            config=self.tasks_config['qa_competitor_report_task'],
            agent=self.qa_competitor_report_agent(),
            output_file = f"results/{self.company_name} analys.md"

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