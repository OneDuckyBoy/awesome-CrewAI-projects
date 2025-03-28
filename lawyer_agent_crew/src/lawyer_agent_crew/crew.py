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
class LegalAgentCrew:

    def __init__(self): 
        _blank = ""
    # no variables needed to be given this project,
    # so i commented it



    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def lead_team_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_team_agent'],
            allow_delegation=True,
            verbose=True,
            tools=[
                # FileReadTool(file_path='research/legal_research.md'),
                # MDXSearchTool(mdx='research/legal_research.md')
            ]
        )
    @task
    def lead_team_task(self)-> Task:
        return Task(
            config=self.tasks_config['lead_team_task'],
            agent=self.lead_team_agent(),
            allow_delegation=True,
            tools=[
                # FileReadTool(file_path='research/legal_research.md'),
                # MDXSearchTool(mdx='research/legal_research.md')
            ],
        )

    @agent
    def web_research_agent(self) -> Agent:
        search_tool = SerperDevTool()

        return Agent(
            config=self.agents_config['web_research_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            output= f"results/legal_research.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file = f"results/legal_research.md"
        )
    
    @agent
    def legal_domain_expert_agent(self) -> Agent:
        search_tool = SerperDevTool()
        return Agent(
            config=self.agents_config['legal_domain_expert_agent'],
            allow_delegation=True,
            verbose=True,
            tools=[
                search_tool,
                FileReadTool(file_path='research/legal_research.md'),
                MDXSearchTool(mdx='research/legal_research.md')],
            output= f"results/legal_research.md"
        )
    
    @task
    def legal_domain_expert_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['legal_domain_expert_task'],
            agent=self.legal_domain_expert_agent(),
            tools=[
                search_tool,
                FileReadTool(file_path='research/legal_research.md'),
                MDXSearchTool(mdx='research/legal_research.md')],
            output_file = f"results/legal_research.md"
        )
    

    @agent
    def quality_assurance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='research/legal_research.md'),
                MDXSearchTool(mdx='research/legal_research.md')
            ]
        )
    @task
    def quality_assurance_task(self)-> Task:
        return Task(
            config=self.tasks_config['quality_assurance_task'],
            agent=self.quality_assurance_agent(),
            allow_delegation=True,
            tools=[
                FileReadTool(file_path='research/legal_research.md'),
                MDXSearchTool(mdx='research/legal_research.md')
            ],
        )
    
    
    
    @crew
    def crew(self) -> Crew:
        # if you add examples, add them to the knowledge folder and uncomment the lines and add the correct filenames, 
        # starting from the knowledge as a starting folder
        example_articles = [

    # TextFileKnowledgeSource(file_path="example_analys_1.md"),
    # TextFileKnowledgeSource(file_path="example_analys_2.md"),
]
        return Crew(
            agents=[
            self.web_research_agent(),
            self.legal_domain_expert_agent(),
            self.quality_assurance_agent(),
        ],  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True, 
            knowledge_sources=example_articles,
            manager_agent=self.lead_team_agent(),
        )