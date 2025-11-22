import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "data/cache.db"
BCB_API_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
SECRET_KEY = os.getenv("SECRET_KEY", "dev_key")