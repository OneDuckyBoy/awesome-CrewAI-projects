from typing import List
from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
from crewai_tools import SerperDevTool,MDXSearchTool,FileReadTool # type: ignore
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

os.environ["SERPER_API_KEY"] =os.getenv("SERPER_API_KEY")


@CrewBase
class SubjectTeachingCrew:

    def __init__(self, subject):
        self.subject = subject


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
            output=f"research/{self.subject}.md"
        )
    
    @task
    def web_research_task(self) -> Task:
        search_tool = SerperDevTool()

        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            tools=[search_tool],
            output_file = f"research/{self.subject}.md"

        )

    @agent
    def lesson_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_writer_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[
                FileReadTool(file_path='research/'+self.subject+'.md'),
                MDXSearchTool(mdx='research/'+self.subject+'.md')
            ]
        )
    @task
    def lesson_writer_task(self)-> Task:
        return Task(
            config=self.tasks_config['lesson_writer_task'],
            agent=self.lesson_writer_agent(),
            allow_delegation=False,
            tools=[
                FileReadTool(file_path='research/'+self.subject+'.md'),
                MDXSearchTool(mdx='research/'+self.subject+'.md')
            ],
        )
    @agent
    def qa_teacher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_teacher_agent'],
            allow_delegation=True,
            verbose=True,
            output_file = f"results/{self.subject}.md"

        )
    @task
    def qa_teacher_task(self) -> Task:
        task = Task(
            config=self.tasks_config['qa_teacher_task'],
            agent=self.qa_teacher_agent(),
            output_file = f"results/{self.subject}.md"

        )
    

        return task


    # @agent
    # def senior_test_writer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['senior_test_writer'],
    #         allow_delegation=False,
    #         verbose=True
    #     )
    
    # @agent
    # def qa_test_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['qa_test_agent'],
    #         allow_delegation=False,
    #         verbose=True
    #     )
    
    # @agent
    # def chief_qa_teacher_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['chief_qa_teacher_agent'],
    #         allow_delegation=True,
    #         verbose=True,
    #     )
    

    # @task
    # def write_test_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['write_test_task'],
    #         agent=self.senior_test_writer()
    #     )

    # @task
    # def review_test_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['review_test_task'],
    #         agent=self.qa_test_agent(),
    #     )
    # @task
    # def final_check_test_task(self) -> Task:
        # task = Task(
        #     config=self.tasks_config['final_check_test_task'],
        #     agent=self.chief_qa_teacher_agent(),
        #     output_file="results/recommendations.md"
        # )
    

        # return task

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilderCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
        )