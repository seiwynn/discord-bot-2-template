import sys
from src import bot
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    bot.run_discord_bot()