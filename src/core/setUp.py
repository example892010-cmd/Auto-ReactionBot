import os
import logging
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

# Load local .env file if it exists (automatically ignored on Render)
load_dotenv()

# Setup logging and suppress noisy library logs
logging.basicConfig(level=logging.INFO)
logging.getLogger("aiosqlite").setLevel(logging.ERROR)

# Safely look for your token across multiple variable names, with your token as a failsafe backup
Token = (
    os.getenv("BOT_TOKEN") or 
    os.getenv("TELEGRAM_TOKEN") or 
    os.getenv("API_TOKEN") or 
    "8577590790:AAFzZxa-yhOYCI-tC32N3z5bslW8pGKv5lU"
)

if not Token:
    raise ValueError("Telegram Bot Token is missing! Please set BOT_TOKEN in Render environment variables.")

# Initialize the Async Telegram Bot
Bot = AsyncTeleBot(Token)
