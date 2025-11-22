from agno.agent import Agent
from tools.cdi_tool import CdiTool
from tools.selic_tool import SelicTool

class RendaFixaAgent(Agent):
    tools = [CdiTool(), SelicTool()]
