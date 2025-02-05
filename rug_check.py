import requests
from dotenv import load_dotenv
import os

load_dotenv()

class RugChecker:
    def __init__(self):
        self.api_key = os.getenv('RUGCHECK_API_KEY')
    
    def check_rug(self, contract_address):
        headers = {'x-api-key': self.api_key}
        response = requests.get(
            f'https://rugcheck.xyz/api/v1/tokens/solana/{contract_address}/report',
            headers=headers
        )
        data = response.json()
        return {
            'is_rug': data['rugStatus']['isRug'],
            'score': data['rugStatus']['rugScore']
        }
