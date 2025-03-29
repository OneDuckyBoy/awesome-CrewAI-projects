from typing import List
from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
from crewai_tools import SerperDevTool,MDXSearchTool,FileReadTool,VisionTool # type: ignore
# import os
# from dotenv import load_dotenv # type: ignore
# load_dotenv()

# os.environ["SERPER_API_KEY"] =os.getenv("SERPER_API_KEY")

import os
@CrewBase
class SolveCodeErrorFromImageCrew:
    def __init__(self):
        self.error_image_path = os.path.abspath("errorImageFolder/error.png")
        self.vision_tool = VisionTool(image_path_url=self.error_image_path) 
        


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def get_text_from_image_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config['get_text_from_image_agent'],
            allow_delegation=False,
            verbose=True,
            tools=[self.vision_tool],
            # output=f"results/imageText.md"
        )
    
    @task
    def get_text_from_image_task(self) -> Task:
        
        return Task(
            config=self.tasks_config['get_text_from_image_task'],
            agent=self.get_text_from_image_agent(),
            tools=[self.vision_tool],
            output_file = f"results/imageText.md"

        )

    @agent
    def fix_error_from_code_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fix_error_from_code_agent'],
            allow_delegation=False,
            verbose=True,
            # tools=[
            #     FileReadTool(file_path='research/'+self.subject+'.md'),
            #     MDXSearchTool(mdx='research/'+self.subject+'.md')
            # ]
        )
    @task
    def fix_error_from_code_task(self)-> Task:
        return Task(
            config=self.tasks_config['fix_error_from_code_task'],
            agent=self.fix_error_from_code_agent(),
            allow_delegation=False,
            output_file = f"results/fixed_code.md"
        )
    # @agent
    # def qa_teacher_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['qa_teacher_agent'],
    #         allow_delegation=True,
    #         verbose=True,
    #         output_file = f"results/{self.subject}.md"

    #     )
    # @task
    # def qa_teacher_task(self) -> Task:
    #     task = Task(
    #         config=self.tasks_config['qa_teacher_task'],
    #         agent=self.qa_teacher_agent(),
    #         output_file = f"results/{self.subject}.md"
    #     )
    #     return task


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