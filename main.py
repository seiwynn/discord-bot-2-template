import sys
from src import bot
from dotenv import load_dotenv



def check_library_versions() -> None:
    load_dotenv()
    # TODO: check library versions based on requirements.txt
    pass


if __name__ == '__main__':
    check_library_versions()
    bot.run_discord_bot()
