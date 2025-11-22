from services.sgs_api import SGSApi

class InflationService:
    def get_ipca(self):
        return SGSApi().get_series(433)
