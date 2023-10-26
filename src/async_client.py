import os
import json
import discord
import asyncio
import typing

from dotenv import load_dotenv
load_dotenv()

class AsyncClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.tree = discord.app_commands.CommandTree(self)
        self.current_channel = None
        self.activity = discord.Activity(
            type=discord.ActivityType.watching, name="over Hitomi's tasks")

client = AsyncClient()
