import os
from src import bot
from dotenv import load_dotenv



def check_library_versions() -> None:
    load_dotenv()
    # TODO: check library versions based on requirements.txt
    pass


if __name__ == '__main__':
    check_library_versions()
    token = os.getenv("DISCORD_BOT_TOKEN")
    client = bot.Bot(token)
    client.run(client.token)

