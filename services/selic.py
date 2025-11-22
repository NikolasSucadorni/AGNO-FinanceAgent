from services.sgs_api import SGSApi

class SelicService:
    def get_selic(self):
        return SGSApi().get_series(432)
