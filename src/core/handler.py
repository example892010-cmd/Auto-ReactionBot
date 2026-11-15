from telebot.types import ReactionTypeEmoji
from src.core.setUp import Bot

@Bot.message_handler(func=lambda message: True)
async def auto_react(message):
    """
    Automatically reacts to any incoming message with a specified emoji.
    """
    try:
        # You can change '👍' to any other valid Telegram reaction emoji (e.g., '🔥', '❤️', '👏')
        await Bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            reaction=[ReactionTypeEmoji('👍')],
            is_big=False
        )
    except Exception as e:
        print(f"Error applying reaction: {e}")
