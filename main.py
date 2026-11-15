import asyncio
import logging
import aiosqlite
from src.core.setUp import Bot

# Import slashCommands and core handlers so all commands and event listeners register
import src.slashCommands
import src.core

async def init_db():
    """Ensure Database.db has the required tables from db.schema."""
    async with aiosqlite.connect("Database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS `Groups` (
                `chatId` INTEGER,
                `Word` TEXT,
                `Reaction` TEXT,
                `mentionReaction` INTEGER,
                `mentionReactionBig` INTEGER,
                `replyReaction` INTEGER,
                `replyReactionBig` INTEGER
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS `Users` (
                `userId` INTEGER
            );
        """)
        await db.commit()

async def main():
    logging.info("🤖 Starting Auto-ReactionBot...")
    await init_db()
    # Clear any leftover webhook before starting polling
    await Bot.remove_webhook()
    # Start continuous polling
    await Bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    asyncio.run(main())
