import os
from telebot.async_telebot import AsyncTeleBot

# Checks Render's environment across all common names, with your token as a permanent fallback
Token = (
    os.getenv("BOT_TOKEN") or 
    os.getenv("TELEGRAM_TOKEN") or 
    os.getenv("API_TOKEN") or 
    "8577590790:AAFzZxa-yhOYCI-tC32N3z5bslW8pGKv5lU"
)

if not Token:
    raise ValueError("Telegram Bot Token is missing!")

Bot = AsyncTeleBot(Token)

# Define log directory
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# 
logging.getLogger("aiosqlite").setLevel(logging.ERROR)

# Advanced logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set the base logging level
    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s',  # Custom log format
    datefmt='%Y-%m-%d %H:%M:%S',  # Custom date format
    handlers=[  # Multiple handlers
        logging.StreamHandler(sys.stdout),  # Log to console
        RotatingFileHandler(
            os.path.join(log_dir, 'app.log'),  # Log file
            maxBytes=5 * 1024 * 1024,  # 5MB per log file
            backupCount=3,  # Keep 3 old log files
            encoding='utf-8'
        ),  
        TimedRotatingFileHandler(
            os.path.join(log_dir, 'timed_log.log'),  # Separate log for timed rotation
            when="midnight",  # Rotate at midnight
            interval=1,  # Rotate every 1 day
            backupCount=7,  # Keep the last 7 days of logs
            encoding='utf-8'
        ),
    ]
)

validEmojis = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]
