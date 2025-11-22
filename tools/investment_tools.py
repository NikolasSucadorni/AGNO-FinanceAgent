from agno.tools import tool

@tool
def compare_investments(amount: float, rate1: float, rate2: float, months: int):
    """
    Compara dois investimentos usando juros compostos.

    amount -> valor inicial aplicado
    rate1 -> taxa mensal do investimento 1 (ex: 0.01 = 1% a.m.)
    rate2 -> taxa mensal do investimento 2
    months -> prazo em meses
    """

    final1 = amount * ((1 + rate1) ** months)
    final2 = amount * ((1 + rate2) ** months)

    melhor = "Investimento 1" if final1 > final2 else "Investimento 2"

    return {
        "valor_inicial": amount,
        "prazo_meses": months,
        "investimento_1_final": round(final1, 2),
        "investimento_2_final": round(final2, 2),
        "melhor_investimento": melhor,
        "mensagem": f"O {melhor} rende mais após {months} meses."
    }
