import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "question": "Тестовый опрос",
        "options": ["Да", "Нет", "Возможно"],
        "is_anonymous": False
    }
)

print(response.text)
