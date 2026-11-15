import asyncio
from src.core.setUp import Bot

# Import handlers so they register their event listeners with the bot instance
import src.core.handler

async def main():
    print("🤖 Starting Auto-ReactionBot...")
    # Clear any leftover webhooks before starting polling
    await Bot.remove_webhook()
    # Start receiving updates
    await Bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())
