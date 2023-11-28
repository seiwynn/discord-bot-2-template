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
            type=discord.ActivityType.watching, name="my empty description")


# this should be the only actual discord client existing.
class SingletonClient():
    # type: discord.Client
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = AsyncClient()
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None

