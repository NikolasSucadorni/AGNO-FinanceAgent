from agno.tools import tool
import requests

@tool
def obter_selic():
    """
    Retorna a taxa SELIC diária e anual.
    """
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()

        dados = resp.json()
        ultima = dados[-1]

        # Corrigido: valor vem como porcentagem diária
        selic_diaria_percent = float(ultima["valor"])        # ex: 0.055131 (%)
        selic_diaria = selic_diaria_percent / 100            # converter para decimal

        # anualização correta
        selic_anual = (1 + selic_diaria) ** 252 - 1

        return {
            "ok": True,
            "data": ultima["data"],
            "selic_diaria_percentual": round(selic_diaria_percent, 6),
            "selic_diaria_decimal": selic_diaria,
            "selic_anual_percentual": round(selic_anual * 100, 4),
        }

    except Exception:
        return {
            "ok": False,
            "mensagem": "Não foi possível acessar o BCB no momento."
        }
