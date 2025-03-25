from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool



@CrewBase
class TestWriterCrew:
    """TestWriter crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def senior_test_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_test_writer'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def qa_test_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_test_agent'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def chief_qa_teacher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_qa_teacher_agent'],
            allow_delegation=True,
            verbose=True
        )
    

    @task
    def write_test_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_test_task'],
            agent=self.senior_test_writer()
        )

    @task
    def review_test_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_test_task'],
            agent=self.qa_test_agent(),
            #### output_json=ResearchRoleRequirements
        )
    # self.crew.register_tool("file_writer", FileWriterTool)
    @task
    def final_check_test_task(self) -> Task:
        # main_topic = task.inputs.get("main_topic", "topic")  # Use a default if not found
        
        # file_writer = FileWriterTool(path="../tests/{main_topic}.txt", mode="w")

        # test_content = "Test content based on the topic: {main_topic}" 

        # Execute the tool (write to file)
        # file_writer.execute(test_content)
        task = Task(
            config=self.tasks_config['final_check_test_task'],
            agent=self.chief_qa_teacher_agent(),
            # tools=[file_writer]
        )
    

        return task

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilderCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
        )