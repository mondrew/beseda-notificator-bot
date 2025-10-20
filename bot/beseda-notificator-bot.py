import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BESEDA_NOTIFICATOR_BOT_TOKEN")
CHAT_ID = os.getenv("BESEDA_NOTIFICATOR_BOT_CHAT_ID")


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    print(url)
    r = requests.post(url, json={"chat_id": CHAT_ID, "text": text}, timeout=20)
    print(r.status_code, r.text)

if __name__ == "__main__":
    send_message("Hello! 🚀 Notification bot is working.")
