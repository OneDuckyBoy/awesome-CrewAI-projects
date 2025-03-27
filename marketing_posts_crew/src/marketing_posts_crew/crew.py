from typing import List
from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
from crewai_tools import SerperDevTool,MDXSearchTool,FileReadTool,DallETool # type: ignore
from datetime import datetime
import shutil
import os
from dotenv import load_dotenv # type: ignore
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
# instagram agents and tasks
    @agent
    def instagram_trending_post_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['instagram_trending_post_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def instagram_trending_post_generator_task(self) -> Task:
        source_folder = 'posts/Instagram'
        destination_folder = 'posts/Instagram/old posts'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['instagram_trending_post_generator_task'],
            agent=self.instagram_trending_post_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/Instagram/Instagram_post "+formatted_datetime+".txt"
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
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['dall_e_promt_task'],
            agent=self.instagram_dall_e_prompt_agent(),
            context=[self.instagram_trending_post_generator_task()],
            output_file="posts/Instagram/Instagram post picture "+formatted_datetime+".txt"
           
        )
# FaceBook agents and tasks
    @agent
    def facebook_trending_post_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['facebook_trending_post_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def facebook_trending_post_generator_task(self) -> Task:
        source_folder = 'posts/Facebook'
        destination_folder = 'posts/Facebook/old posts'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['facebook_trending_post_generator_task'],
            agent=self.facebook_trending_post_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/Facebook/Facebook_post "+formatted_datetime+".txt"
        )
    
    @agent
    def facebook_dall_e_prompt_agent(self) -> Task:
        return Agent(
            config=self.agents_config['facebook_dall_e_prompt_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[DallETool()]
        )
    @task
    def facebook_dall_e_promt_task(self) -> Task:
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['dall_e_promt_task'],
            agent=self.facebook_dall_e_prompt_agent(),
            context=[self.facebook_trending_post_generator_task()],
            output_file="posts/Facebook/Facebook post picture "+formatted_datetime+".txt"
           
        )

# X.com agents and tasks
    @agent
    def x_com_trending_post_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['x_com_trending_post_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def x_com_trending_post_generator_task(self) -> Task:

        source_folder = 'posts/X.com'
        destination_folder = 'posts/X.com/old posts'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['x_com_trending_post_generator_task'],
            agent=self.x_com_trending_post_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/X.com/X.com_post "+formatted_datetime+".txt"
        )
    
    @agent
    def x_com_dall_e_prompt_agent(self) -> Task:
        return Agent(
            config=self.agents_config['x_com_dall_e_prompt_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[DallETool()]
        )
    @task
    def x_com_dall_e_promt_task(self) -> Task:
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['dall_e_promt_task'],
            agent=self.x_com_dall_e_prompt_agent(),
            context=[self.x_com_trending_post_generator_task()],
            output_file="posts/X.com/X.com post picture "+formatted_datetime+".txt"
           
        )

# Threads agents and tasks
    @agent
    def threads_trending_post_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['threads_trending_post_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def threads_trending_post_generator_task(self) -> Task:

        source_folder = 'posts/Threads'
        destination_folder = 'posts/Threads/old posts'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['threads_trending_post_generator_task'],
            agent=self.threads_trending_post_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/Threads/Threads_post "+formatted_datetime+".txt"
        )
    
    @agent
    def threads_dall_e_prompt_agent(self) -> Task:
        return Agent(
            config=self.agents_config['threads_dall_e_prompt_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[DallETool()]
        )
    @task
    def threads_dall_e_promt_task(self) -> Task:
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['dall_e_promt_task'],
            agent=self.threads_dall_e_prompt_agent(),
            context=[self.threads_trending_post_generator_task()],
            output_file="posts/Threads/Threads post picture "+formatted_datetime+".txt"
           
        )
    
# email newsletter agents and tasks
    @agent
    def email_newsletter_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_newsletter_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def email_newsletter_generator_task(self) -> Task:

        source_folder = 'posts/Email newsletter'
        destination_folder = 'posts/Email newsletter/old newsletters'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['email_newsletter_generator_task'],
            agent=self.email_newsletter_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/Email newsletter/email_newsletter "+formatted_datetime+".txt"
        )
    
# marketing email agents and tasks
    @agent
    def email_marketing_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_marketing_generator_agent'],
            allow_delegation=False,
            verbose=True
        )
    @task
    def email_marketing_generator_task(self) -> Task:

        source_folder = 'posts/Email Marketing'
        destination_folder = 'posts/Email Marketing/old email marketing'

        # Ensure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            if os.path.isfile(source_path):  # Check if it's a file
                shutil.move(source_path, destination_path)
        
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
        return Task(
            config=self.tasks_config['email_marketing_generator_task'],
            agent=self.email_marketing_generator_agent(),
            context=[self.web_research_task(), self.company_info_analys_task(), self.read_and_get_all_posts_task()],
            output_file="posts/Email Marketing/email_marketing "+formatted_datetime+".txt"
        )
    
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
        )