from agno.tools import tool
import requests

@tool
def get_bcb_selic():
    """
    Busca a SELIC diária mais recente no SGS do Banco Central.
    """
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()

        dados = resp.json()

        # Verificação forte: o retorno PRECISA ser lista e ter item
        if not isinstance(dados, list) or len(dados) == 0:
            return {
                "ok": False,
                "mensagem": "BCB retornou um formato inesperado (não é lista)."
            }

        dado = dados[0]  # <- CORRIGIDO: nunca usar índice negativo!

        valor_percent = float(dado["valor"])
        valor_decimal = valor_percent / 100

        selic_anual = (1 + valor_decimal) ** 252 - 1

        return {
            "ok": True,
            "data": dado["data"],
            "selic_diaria_percentual": round(valor_percent, 6),
            "selic_diaria_decimal": valor_decimal,
            "selic_anual_percentual": round(selic_anual * 100, 4)
        }

    except Exception as e:
        return {
            "ok": False,
            "mensagem": f"Erro ao acessar o BCB: {str(e)}"
        }
