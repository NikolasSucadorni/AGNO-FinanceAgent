from services.sgs_api import SGSApi

class CDIService:
    def get_cdi(self):
        return SGSApi().get_series(4389)
