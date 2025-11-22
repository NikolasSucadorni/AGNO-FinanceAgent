from agno.agent import Agent
from tools.ipca_tool import IpcaTool

class FIIAgent(Agent):
    tools = [IpcaTool()]
