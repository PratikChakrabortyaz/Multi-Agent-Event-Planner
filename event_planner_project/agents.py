from smolagents import ToolCallingAgent
from smolagents import HfApiModel
from tools import theme_search_tool,catering_search_tool,entertainment_search_tool,decoration_search_tool
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
# Load Hugging Face Token
HF_TOKEN =  user_secrets.get_secret("HF_TOKEN")

theme_agent = ToolCallingAgent(
    tools=[theme_search_tool],
    model=HfApiModel(
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=HF_TOKEN   # Add the token here
    ),
    max_steps=5,
    name="Theme Agent",
    description="Finds creative and trending party themes."
)
catering_agent = ToolCallingAgent(
    tools=[catering_search_tool],
    model=HfApiModel(
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=HF_TOKEN
    ),
    max_steps=5,
    name="Catering Agent",
    description="Suggests catering services for themed events."
)
entertainment_agent = ToolCallingAgent(
    tools=[entertainment_search_tool],
    model=HfApiModel(
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=HF_TOKEN
    ),
    max_steps=5,
    name="Entertainment Agent",
    description="Finds entertainment ideas for themed parties."
)
decoration_agent = ToolCallingAgent(
    tools=[decoration_search_tool],
    model=HfApiModel(
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=HF_TOKEN
    ),
    max_steps=5,
    name="Decoration Agent",
    description="Suggests decoration ideas for themed parties."
)
