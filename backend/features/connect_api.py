import requests
from dotenv import load_dotenv
import os

class Market:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    def __init__(self):
        self.data = self.get_data()
    
    def get_data(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={self.api_key}'
        r = requests.get(url)
        data = r.json()
        return data