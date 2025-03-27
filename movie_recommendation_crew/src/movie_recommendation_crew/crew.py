from typing import List
from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
# from crewai_tools import FileWriterTool



@CrewBase
class MovieRecommendationCrew:
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
            verbose=True,
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
        )
    @task
    def final_check_test_task(self) -> Task:
        task = Task(
            config=self.tasks_config['final_check_test_task'],
            agent=self.chief_qa_teacher_agent(),
            output_file="results/recommendations.md"
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