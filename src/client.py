import os
import json
import discord
import asyncio
import typing

from dotenv import load_dotenv
load_dotenv()


class Client(discord.Client):

    def __init__(
        self,
        token: str,
        intents: discord.Intents = discord.Intents(messages=True)
    ):
        super().__init__(intents=intents)
        self.token = token
        self.tree = discord.app_commands.CommandTree(self)
        self.current_channel = None

        self.activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="my empty description"
        )

    @staticmethod
    def get_cmd_header(
        id: int,
        title: str
    ) -> str:
        return f'> **{title}** - <@{str(id)}> \n\n'


# not necessary, but if you want to use the same client everywhere
class SingletonClient():
    # type: discord.Client
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = Client()
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None
