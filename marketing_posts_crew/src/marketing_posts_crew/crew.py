from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,MDXSearchTool,FileReadTool,DallETool
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["SERPER_API_KEY"] =os.getenv("SERPER_API_KEY")
@CrewBase
class MarketingPostsCrew:
    """Marketing posts crew"""
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
            output="posts/post trending and email marketing and newsletters analys.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file="posts/post trending and email marketing and newsletters analys.md"
        )

    @agent
    def company_info_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['company_info_analyzer_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='./config/marketing_information.md'),
                MDXSearchTool(mdx='./config/marketing_information.md')
            ]
        )
    
    @task
    def company_info_analys_task(self)-> Task:
        return Task(
            config=self.tasks_config['company_info_analys_task'],
            agent=self.company_info_analyzer_agent(),
            tools=[
                FileReadTool(file_path='./config/marketing_information.md'),
                MDXSearchTool(mdx='./config/marketing_information.md')
            ],
        )
    
    @task
    def read_and_get_all_posts_task(self) -> Task:
        
        def read_posts_recursively():
            all_posts = ""
            for root, _, files in os.walk("./posts"):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    tool = FileReadTool(file_path=file_path)
                    all_posts += tool.run() + "\n"
            return all_posts

        return Task(
            config=self.tasks_config['company_info_analys_task'],
            agent=self.company_info_analyzer_agent(),
            custom_function=read_posts_recursively
        )

    @agent
    def instagram_trending_post_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['instagram_trending_post_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def instagram_trending_post_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['instagram_trending_post_generator_task'],
            agent=self.instagram_trending_post_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/instagram_post.md"
        )
    
    @agent
    def instagram_dall_e_prompt_agent(self) -> Task:
        return Agent(
            config=self.agents_config['instagram_dall_e_prompt_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[DallETool()]
        )
    @task
    def instagram_dall_e_promt_task(self) -> Task:
        return Task(
            config=self.tasks_config['dall_e_promt_task'],
            agent=self.instagram_dall_e_prompt_agent(),
            context=[self.instagram_trending_post_generator_task()],
            output_file="posts/Instagram post picture.txt"
           
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
        )