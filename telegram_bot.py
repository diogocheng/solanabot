import requests
from dotenv import load_dotenv
import os

load_dotenv()

class TelegramBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')

    async def send_alert(self, token_data, probability):
        message = (
            f"Potential Trade Alert!\n"
            f"Token: {token_data.get('name', 'Unknown')}\n"
            f"Predicted Success Probability: {probability:.2f}\n"
            f"Address: {token_data.get('address')}"
        )
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(url, json=payload)
        print("Telegram response:", response.json())
