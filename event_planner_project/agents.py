from smolagents import ToolCallingAgent
from smolagents import HfApiModel
from tools import theme_search_tool

theme_agent = ToolCallingAgent(
    tools=[theme_search_tool],
    model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct"),
    max_steps=5,
    name="Theme Agent",
    description="Finds creative and trending party themes."
)
