from agno.tools import tool
import requests

@tool
def obter_ipca():
    """
    Retorna o IPCA mais recente (mensal e acumulado em 12 meses)
    usando os dados do Banco Central (série SGS 433).
    """
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()
    except Exception:
        return {
            "ok": False,
            "mensagem": "Erro ao consultar o IPCA no Banco Central."
        }

    if not dados:
        return {
            "ok": False,
            "mensagem": "Nenhum dado encontrado para a série do IPCA."
        }

    # Último IPCA mensal
    ultimo = dados[-1]
    ipca_mensal = float(ultimo["valor"])
    data = ultimo["data"]

    # Cálculo do IPCA acumulado em 12 meses
    try:
        ultimos_12 = dados[-12:]
        acumulado = 1
        for item in ultimos_12:
            acumulado *= (1 + float(item["valor"]) / 100)
        ipca_12m = (acumulado - 1) * 100
    except:
        ipca_12m = None

    return {
        "ok": True,
        "data": data,
        "ipca_mensal_percentual": round(ipca_mensal, 4),
        "ipca_12m_percentual": round(ipca_12m, 4) if ipca_12m else None,
        "mensagem": (
            f"O IPCA mais recente é {round(ipca_mensal,4)}% "
            f"(data: {data}). "
            f"IPCA acumulado em 12 meses: {round(ipca_12m,4)}%."
        )
    }
