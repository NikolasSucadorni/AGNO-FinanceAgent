from agno.agent import Agent
from tools.bcb_api import BCBTool
from tools.investment_tools import InvestmentComparisonTool
from services.monte_carlo import MonteCarlo
from memory.memory_service import MemoryService


class MainAgent(Agent):
    """
    Agente principal que orquestra os outros agentes.
    Ele pode:
    - buscar CDI, SELIC e IPCA via API do Banco Central (SGS)
    - simular investimentos
    - comparar ativos (renda fixa, FII, cripto)
    - usar memória financeira
    - rodar Monte Carlo
    """

    def __init__(self):
        super().__init__(
            name="FinanceAI Main Agent",
            role="Agente financeiro especialista",
            goal="Auxiliar o usuário com análises financeiras completas",
            tools=[
                BCBTool(),
                InvestmentComparisonTool(),
            ],
            memory=MemoryService().get_memory(),
        )

        # Sub-agentes opcionais (estrutura escalável)
        self.monte_carlo = MonteCarlo()

    def analyze(self, query: str) -> str:
        """
        Decide qual ferramenta usar com base na pergunta
        (roteador simples — pode ficar mais inteligente depois).
        """
        query_lower = query.lower()

        # ---- Dados macroeconômicos ----
        if "cdi" in query_lower or "selic" in query_lower or "ipca" in query_lower:
            return self.run_tool("bcb_api", query)

        # ---- Comparação de investimentos ----
        if "comparar" in query_lower or "melhor investimento" in query_lower:
            return self.run_tool("investment_comparison", query)

        # ---- Monte Carlo ----
        if "monte carlo" in query_lower or "simulação" in query_lower:
            params = self._extract_monte_carlo_params(query)
            return self._run_monte_carlo(params)

        # ---- Default ----
        return self.run(query)

    def _run_monte_carlo(self, params):
        result = self.monte_carlo.simulate(
            price=params["price"],
            mean=params["mean"],
            vol=params["vol"],
            days=params["days"],
            sims=params["sims"]
        )
        return f"Resultado da simulação Monte Carlo:\n{result}"

    def _extract_monte_carlo_params(self, query: str):
        # OBS: essa função pode virar um parser inteligente mais tarde
        # Por enquanto, retornamos valores padrão
        return {
            "price": 100,
            "mean": 0.08,
            "vol": 0.15,
            "days": 365,
            "sims": 500
        }
