import requests
import pandas as pd
from config.settings import BCB_API_URL

class SGSApi:
    def get_series(self, code):
        url = BCB_API_URL.format(code=code)
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df['valor'] = df['valor'].astype(float)
        return df
