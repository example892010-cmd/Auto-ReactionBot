import os
import logging
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

# Load local .env file if present
load_dotenv()

# Configure logging and silence noisy aiosqlite logs
logging.basicConfig(level=logging.INFO)
logging.getLogger("aiosqlite").setLevel(logging.ERROR)

# List of valid Telegram reaction emojis required by slashCommands
validEmojis = [
    "👍", "👎", "❤", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢",
    "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥",
    "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋",
    "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝",
    "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄",
    "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"
]

# Check the original repo's 'Token' variable first, then common alternatives
raw_token = (
    os.getenv("Token") or 
    os.getenv("BOT_TOKEN") or 
    os.getenv("TELEGRAM_TOKEN") or 
    os.getenv("API_TOKEN") or 
    "8577590790:AAFzZxa-yhOYCI-tC32N3z5bslW8pGKv5lU"
)

# Clean any accidental quotes or whitespace around the token
Token = raw_token.strip().strip('"').strip("'") if raw_token else None

if not Token:
    raise ValueError("Bot Token is missing! Set 'Token' or 'BOT_TOKEN' in Render Environment Variables.")

# Initialize the AsyncTeleBot instance
Bot = AsyncTeleBot(Token)
