import os
import asyncio
import discord
from src.async_client import SingletonClient
from utils.fileio import read

# ty design pattern class



def run_discord_bot(token: str):
    client = SingletonClient()

    @client.event
    async def on_ready():
        await client.tree.sync()

    @client.event
    async def on_message(message: discord.Message):
        # print(f"Message received: {message.content}")
        # skip slash commands
        if message.type is discord.MessageType.chat_input_command:
            return
        # skip if it's the bot itself
        if message.author is client.user:
            return

        # flags to identify source of message
        is_dm = not message.guild
        is_mentioned = client.user in message.mentions

        # TODO: handle the msg however you want

        # https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working
        # but apparently we don't need this anymore
        # await client.process_commands(message)

    @client.tree.command(name="help", description="readme")
    async def help(interaction: discord.Interaction):
        # should be relative to root directory
        help_doc_location = "assets/docs/help.md"
        help_message = read(help_doc_location)
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(help_message)

    client.run(token)
