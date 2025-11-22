from agno.tools import tool

@tool
def calcular_portfolio(aportes: dict):
    """
    Soma todos os valores de um portfólio.
    Exemplo de entrada:
        {"Tesouro Selic": 1000, "CDB": 2000}
    """
    total = sum(aportes.values())
    return f"O valor total investido é R$ {total:.2f}"
