import requests

class DexScreener:
    def __init__(self):
        self.base_url = "https://api.dexscreener.com/latest/dex"
    
    def get_low_mcap_tokens(self):
        params = {
            'chain': 'solana',
            'sort': 'createdAt',
            'order': 'asc'
        }
        response = requests.get(f"{self.base_url}/tokens", params=params)
        return [token for token in response.json()['results'] if token.get('marketCap', float('inf')) < 200000]
