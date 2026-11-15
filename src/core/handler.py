import logging
from telebot.types import ReactionTypeEmoji
from src.core.setUp import Bot
from src.core.Database import checkUsersGroup, checkUserInfo

logging.info(f"Added {__name__}")

@Bot.message_handler(func=lambda message: message.chat.type in ['group', 'supergroup'] and bool(message.text and not message.text.startswith('/')))
async def handleGroupAutoReaction(message):
    """
    Scans group messages for matching configured words or replied-to usernames
    and applies the configured emoji reaction from Database.db.
    """
    chatId = message.chat.id
    words = await checkUsersGroup(chatId)
    if not words:
        return

    text_words = message.text.split() if message.text else []

    # 1. Scan message for matching words/mentions first
    for w in text_words:
        if w in words:
            userData = await checkUserInfo(chatId, w)
            # Schema: (chatId, Word, Reaction, mentionReaction, mentionReactionBig, replyReaction, replyReactionBig)
            if userData and userData[3]:  # mentionReaction enabled
                try:
                    await Bot.set_message_reaction(
                        chat_id=chatId,
                        message_id=message.id,
                        reaction=[ReactionTypeEmoji(userData[2])],
                        is_big=bool(userData[4])
                    )
                except Exception as e:
                    logging.error(f"Error setting mention reaction: {e}")
                return

    # 2. If it's a reply and no matching words were found in text, check replied-to username
    if message.reply_to_message and message.reply_to_message.from_user:
        replied_username = message.reply_to_message.from_user.username
        if replied_username:
            target = f"@{replied_username}"
            if target in words:
                userData = await checkUserInfo(chatId, target)
                if userData and userData[5]:  # replyReaction enabled
                    try:
                        await Bot.set_message_reaction(
                            chat_id=chatId,
                            message_id=message.id,
                            reaction=[ReactionTypeEmoji(userData[2])],
                            is_big=bool(userData[6])
                        )
                    except Exception as e:
                        logging.error(f"Error setting reply reaction: {e}")
                    return
