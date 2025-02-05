import asyncio
from dotenv import load_dotenv
from ml_model import MLModel
from dex_manager import DexScreener
from rug_check import RugChecker
from solana_verify import SolanaVerifier
from telegram_bot import TelegramBot

load_dotenv()

class TradingBot:
    def __init__(self):
        self.ml = MLModel()
        self.dex = DexScreener()
        self.rug_check = RugChecker()
        self.solana = SolanaVerifier()
        self.tg = TelegramBot()
    
    async def analyze_token(self, token):
        try:
            features = [
                token['liquidity']['usd'],
                token['volume']['h24'],
                token['priceChange']['h24'],
                token['txns']['h24']['buys'] / token['txns']['h24']['sells'] if token['txns']['h24']['sells'] != 0 else 0
            ]
        except KeyError as e:
            print(f"Missing key in token data: {e}")
            return 0.0
        return self.ml.predict(features)
    
    async def monitor(self):
        while True:
            tokens = self.dex.get_low_mcap_tokens()
            for token in tokens:
                if (self.solana.verify_token(token['address']) and 
                    not self.rug_check.check_rug(token['address'])['is_rug']):
                    probability = await self.analyze_token(token)
                    if probability > 0.75:
                        await self.tg.send_alert(token, probability)
            await asyncio.sleep(300)

if __name__ == "__main__":
    bot = TradingBot()
    asyncio.run(bot.monitor())


