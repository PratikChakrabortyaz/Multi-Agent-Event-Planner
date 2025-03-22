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
- Use `theme_agent()` for themes.
- Use `catering_agent()` for catering.
- Use `entertainment_agent()` for entertainment.
- Use `decoration_agent()` for decorations.

Here’s the exact code template to follow:

def theme_agent():
    return tools['theme_agent'].run("Suggest a superhero party theme.")

def catering_agent():
    return tools['catering_agent'].run("Suggest superhero-themed catering ideas.")

def entertainment_agent():
    return tools['entertainment_agent'].run("Suggest superhero-themed entertainment ideas.")

def decoration_agent():
    return tools['decoration_agent'].run("Suggest superhero-themed decorations.")

theme = theme_agent()
decorations = decoration_agent()
catering = catering_agent()
entertainment = entertainment_agent()

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
    tools={
        "theme_agent": theme_agent,
        "catering_agent": catering_agent,
        "entertainment_agent": entertainment_agent,
        "decoration_agent": decoration_agent
    },
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

