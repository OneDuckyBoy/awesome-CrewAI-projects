# AI Crew for making posts for most popular social medias and email newsletters/marketing
## Introduction
This project demonstrates the use of the CrewAI framework to automate the creation tests on different topics. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

  ## Example posts from the marketing posts crew:
  <picture>
      <source media="(prefers-color-scheme: dark)" srcset="4 posts.png">
      <img src="4 posts.png" alt="4 example posts image" width="1000" />
    </picture>

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, The agents work together to build a Python-based game by simulating a collaborative software development process. Each agent has a distinct role, from writing the code to reviewing it for errors and ensuring it meets high-quality standards before final approval.


## Running the Script
It uses GPT-4o by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur in different costs.*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and for [Serper](https://serper.dev/).
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/marketing_posts_crew/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/marketing_posts_crew/config/agents.yaml` to update your agents and `src/marketing_posts_crew/config/tasks.yaml` to update your tasks.
- **Execute the Script**:
- Replace 'marketing_information.md' in the config folder with one that is for your company/person
- Run `poetry run marketing_posts_crew` 

## Details & Explanation
- **Running the Script**: Execute `poetry run marketing_posts_crew`. The script will leverage the CrewAI framework to generate a detailed Test
- **Key Components**:
  - `src/marketing_posts_crew/main.py`: Main script file.
  - `src/marketing_posts_crew/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/marketing_posts_crew/config/agents.yaml`: Configuration file for defining agents.
  - `src/marketing_posts_crew/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/marketing_posts_crew/tools`: Contains tool classes used by the agents.

## License
This project is released under the MIT License.
