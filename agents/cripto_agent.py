from agno.agent import Agent
from services.monte_carlo import MonteCarlo

class CriptoAgent(Agent):
    def simulate(self, price, mean, vol):
        return MonteCarlo().simulate(price, mean, vol)
