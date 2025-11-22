from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat

# Tools
from tools.cdi_tool import calcular_cdi
from tools.ipca_tool import obter_ipca
from tools.compare_tool import comparar_investimentos
from tools.portfolio_tool import calcular_portfolio
from tools.bcb_api import get_bcb_selic


def MultiToolAgent():
    return Agent(
        model=OpenAIChat(
            "gpt-4.1-mini",
            temperature=0
        ),
        tools=[
            calcular_cdi,
            obter_ipca,
            comparar_investimentos,
            calcular_portfolio,
            get_bcb_selic
        ],
        instructions=(
            "Você é Carlos, um agente financeiro altamente especializado em cálculos, projeções "
            "e consultas a dados oficiais. "
            
            "=== REGRAS IMPORTANTES ===\n"
            
            "1) Sempre que o usuário pedir SELIC atual, dados do Banco Central ou informações do SGS, "
            "use PRIMEIRO a ferramenta `get_bcb_selic`.\n"
            
            "2) Se `get_bcb_selic` retornar dados válidos, utilize a SELIC diária retornada para cálculos.\n"
            
            "3) Se `get_bcb_selic` falhar, explique claramente o motivo e pergunte ao usuário se deseja "
            "usar uma taxa estimada antes de prosseguir.\n"
            
            "4) Para CDI → sempre use `calcular_cdi`.\n"
            "5) Para IPCA → sempre use `obter_ipca`.\n"
            "6) Para comparar investimentos → sempre use `comparar_investimentos`.\n"
            "7) Para rentabilidade de carteira → sempre use `calcular_portfolio`.\n"
            
            "8) Para previsões ou simulações de investimento, utilize SEMPRE as taxas reais obtidas "
            "pelas ferramentas. Caso não seja possível, informe que será feita uma projeção aproximada "
            "e aguarde aprovação do usuário.\n"
            
            "9) As respostas devem ser organizadas, bonitas e claras. Evite mensagens longas demais "
            "e sempre apresente cálculos e resultados em formato limpo e profissional."
        )
    )
