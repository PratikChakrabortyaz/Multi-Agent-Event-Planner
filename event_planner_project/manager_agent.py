from smolagents import CodeAgent, HfApiModel
from agents import theme_agent, catering_agent, entertainment_agent, decoration_agent
import pandas as pd
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
# Load Hugging Face Token
HF_TOKEN =  user_secrets.get_secret("HF_TOKEN")


# Manager Agent to coordinate all agents
manager_agent = CodeAgent(
    model=HfApiModel(
        "Qwen/Qwen2.5-7B-Chat",
        token=HF_TOKEN
    ),
    tools=[],
    managed_agents=[
        theme_agent,
        catering_agent,
        entertainment_agent,
        decoration_agent
    ],
    additional_authorized_imports=["pandas"],
    max_steps=15,
    name="Manager Agent",
    description="Orchestrates specialized agents to generate a complete party plan."
)
