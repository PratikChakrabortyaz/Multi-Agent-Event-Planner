from smolagents import CodeAgent, HfApiModel,Tool
from agents import theme_agent, catering_agent, entertainment_agent, decoration_agent
import pandas as pd
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
# Load Hugging Face Token
HF_TOKEN =  user_secrets.get_secret("HF_TOKEN")

# Correct Tool Definitions
theme_tool = Tool(name="theme_agent", function=theme_agent.run)
catering_tool = Tool(name="catering_agent", function=catering_agent.run)
entertainment_tool = Tool(name="entertainment_agent", function=entertainment_agent.run)
decoration_tool = Tool(name="decoration_agent", function=decoration_agent.run)

# Improved Prompt for Manager Agent
task_prompt = """
Plan a superhero-themed party with decorations, catering, and entertainment for 20 guests.

For each task:
- Use `tools['theme_agent'].run()` for themes.
- Use `tools['catering_agent'].run()` for catering.
- Use `tools['entertainment_agent'].run()` for entertainment.
- Use `tools['decoration_agent'].run()` for decorations.

Here’s the exact code template to follow:

theme = tools['theme_agent'].run("Suggest a superhero party theme.")
decorations = tools['decoration_agent'].run("Suggest superhero-themed decorations.")
catering = tools['catering_agent'].run("Suggest superhero-themed catering ideas.")
entertainment = tools['entertainment_agent'].run("Suggest superhero-themed entertainment ideas.")

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
        "theme_agent": theme_tool,
        "catering_agent": catering_tool,
        "entertainment_agent": entertainment_tool,
        "decoration_agent": decoration_tool
    },  
    additional_authorized_imports=["pandas"],
    max_steps=15,
    name="Manager Agent",
    description="Orchestrates specialized agents to generate a complete party plan."
)
