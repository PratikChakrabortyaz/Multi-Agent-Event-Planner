from smolagents import CodeAgent, HfApiModel
from agents import theme_agent, catering_agent, entertainment_agent, decoration_agent
import pandas as pd
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
# Load Hugging Face Token
HF_TOKEN =  user_secrets.get_secret("HF_TOKEN")


# Improved Prompt for Manager Agent
task_prompt = """
Plan a superhero-themed party with decorations, catering, and entertainment for 20 guests.
For each task:
- Use `tools['theme_agent'].run()` for themes.
- Use `tools['catering_agent'].run()` for catering.
- Use `tools['entertainment_agent'].run()` for entertainment.
- Use `tools['decoration_agent'].run()` for decorations.

Here’s the exact code template to follow:

theme = self.tools['theme_agent'].run("Suggest a superhero party theme.")
decorations = self.tools['decoration_agent'].run("Suggest superhero-themed decorations.")
catering = self.tools['catering_agent'].run("Suggest superhero-themed catering ideas.")
entertainment = self.tools['entertainment_agent'].run("Suggest superhero-themed entertainment ideas.")

final_answer({
    "theme": theme,
    "decorations": decorations,
    "catering": catering,
    "entertainment": entertainment
})
"""


# Manager Agent to coordinate all agents
manager_agent = CodeAgent(
    model=HfApiModel(
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=HF_TOKEN
    ),
    tools=[],  # Empty since specialized agents manage tools
    managed_agents=[
        theme_agent,
        catering_agent,
        entertainment_agent,
        decoration_agent
    ],
    additional_authorized_imports=["pandas"],
    max_steps=15,
    name="Manager Agent",
    description="Orchestrates specialized agents to generate a complete party plan.",
)

