from agno.tools import tool
import requests

@tool
def calcular_cdi(valor: float, dias: int):
    """
    Calcula rendimento estimado usando a taxa CDI diária real (série 4390 do BCB).
    O valor retornado pelo BCB já é em percentual (% ao dia).
    """
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados/ultimos/1?formato=json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()
    except Exception:
        return {"ok": False, "mensagem": "Erro ao consultar CDI no Banco Central."}

    if not dados:
        return {"ok": False, "mensagem": "Nenhum dado encontrado para o CDI."}

    ultimo = dados[-1]

    # CDI diário em percentual (%)
    cdi_diario_percentual = float(ultimo["valor"])  # ex: 0.0365 (%)

    # Converter para DECIMAL
    cdi_diario = cdi_diario_percentual / 100

    # Cálculo do rendimento composto
    valor_final = valor * (1 + cdi_diario) ** dias
    rendimento = valor_final - valor

    return {
        "ok": True,
        "data": ultimo["data"],
        "cdi_diario_percentual": round(cdi_diario_percentual, 6),
        "cdi_diario_decimal": cdi_diario,
        "valor_inicial": valor,
        "dias": dias,
        "rendimento": round(rendimento, 2),
        "valor_final": round(valor_final, 2),
    }
