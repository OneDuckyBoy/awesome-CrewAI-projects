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
    def fittness_instructor(self) -> Agent:
        return Agent(
            config=self.agents_config['fittness_instructor'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def fittness_meal_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['fittness_meal_planner'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def fittness_and_meal_plan_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['fittness_and_meal_plan_checker'],
            allow_delegation=True,
            verbose=True
        )
    

    @task
    def fittness_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['fittness_plan_task'],
            agent=self.fittness_instructor()
        )

    @task
    def meal_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['meal_plan_task'],
            agent=self.fittness_meal_planner(),
            #### output_json=ResearchRoleRequirements
        )
    # self.crew.register_tool("file_writer", FileWriterTool)
    @task
    def final_check_plans_task(self) -> Task:
        task = Task(
            config=self.tasks_config['final_check_plans_task'],
            agent=self.fittness_and_meal_plan_checker(),
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