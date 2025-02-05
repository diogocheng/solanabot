from solders.pubkey import Pubkey
from solana.rpc.api import Client
from dotenv import load_dotenv
import os

load_dotenv()

class SolanaVerifier:
    def __init__(self):
        self.client = Client(os.getenv('SOLANA_RPC_ENDPOINT'))
    
    def verify_token(self, contract_address):
        try:
            account_info = self.client.get_account_info_json_parsed(
                Pubkey.from_string(contract_address)
            )
            return account_info.value is not None
        except Exception as e:
            print(f"Verification error: {e}")
            return False
