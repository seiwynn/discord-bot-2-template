import os
import asyncio
import discord
from src.async_client import SingletonClient
from utils import path_utils

# ty design pattern class   
client = SingletonClient()

def run_discord_bot():

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
            # ...unless you want to log your own messages
            return 
        
        # flags to identify source of message
        is_dm = not message.guild
        is_mentioned = client.user in message.mentions

        # TODO: handle the msg however you want

        await message.channel.send("use this for dms")

        # https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working
        # but apparently we don't need this anymore?
        # await client.process_commands(message)

    @client.tree.command(name="__template_cmd__", description="template code for a command you want")
    async def template_cmd(interaction: discord.Interaction, *, specified_param: str = ""):
        # ignore self
        if interaction.user == client.user:
            pass

        # interaction.response can be used only once; we'll use it to defer, then followup
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)

        await interaction.followup.send(f"use this method for replying to slash commands")

    @client.tree.command(name="help", description="readme for bot")
    async def help(interaction: discord.Interaction):
        # this should be relative to root directory
        help_doc_location = r"assets/docs/help.md"
        help_message = path_utils.open_file(help_doc_location)
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(help_message)

    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client.run(TOKEN)

