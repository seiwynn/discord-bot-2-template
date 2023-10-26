import os
import asyncio
import discord
from src.async_client import client

def run_discord_bot():
    

    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client.run(TOKEN)
