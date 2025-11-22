from agno.tools import tool

@tool
def comparar_investimentos(
    valor: float,
    taxa_a: float,
    taxa_b: float,
    dias: int
):
    """
    Compara dois investimentos aplicando suas taxas anuais (em %).
    Usa 252 dias úteis.
    """

    # Cálculo do rendimento composto para A
    rendimento_a = valor * ((1 + taxa_a / 100) ** (dias / 252) - 1)

    # Cálculo do rendimento composto para B
    rendimento_b = valor * ((1 + taxa_b / 100) ** (dias / 252) - 1)

    if rendimento_a > rendimento_b:
        melhor = "A"
    elif rendimento_b > rendimento_a:
        melhor = "B"
    else:
        melhor = "igual"

    return {
        "valor_inicial": valor,
        "dias": dias,
        "taxa_a": taxa_a,
        "taxa_b": taxa_b,
        "rendimento_a": round(rendimento_a, 2),
        "rendimento_b": round(rendimento_b, 2),
        "melhor_investimento": melhor,
        "mensagem": (
            f"O investimento {melhor.upper()} rende mais."
            if melhor != "igual"
            else "Ambos rendem exatamente igual."
        )
    }
