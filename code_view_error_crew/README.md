# AI Crew for Making lesson plans on given subjects
## Introduction
This project demonstrates the use of the CrewAI framework to give a detailed lesson plan on given subject. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.


- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, The agents work together to give you a lesson plan for given subject


## Running the Script
It uses GPT-4o by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur in different costs.*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys).
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/code_view_error_crew/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/code_view_error_crew/config/agents.yaml` to update your agents and `src/code_view_error_crew/config/tasks.yaml` to update your tasks.
- **Execute the Script**:
- Enter your desired topic and a title for the file it will be stored(main_topic)
- Run `poetry run code_view_error_crew` 

## Details & Explanation
- **Running the Script**: Execute `poetry run code_view_error_crew`. The script will leverage the CrewAI framework to generate a detailed Test
- **Key Components**:
  - `src/code_view_error_crew/main.py`: Main script file.
  - `src/code_view_error_crew/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/code_view_error_crew/config/agents.yaml`: Configuration file for defining agents.
  - `src/code_view_error_crew/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/code_view_error_crew/tools`: Contains tool classes used by the agents.

## License
This project is released under the MIT License.
