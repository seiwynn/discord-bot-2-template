import discord
from src.async_client import SingletonClient
from utils.fileio import read
from src.message import send_message

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
        # they might be different objects in memory, don't use 'is' operator
        if message.author == client.user:
            return

        # flags to identify source of message
        is_dm = not message.guild
        is_mentioned = client.user in message.mentions

        # TODO: handle the msg however you want

        # https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working
        # but apparently we don't need this anymore
        # await client.process_commands(message)

    # @client.tree.command(name="__template_cmd__", description="template code for a command you want")
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
        help_doc_location = "assets/docs/help.md"
        help_message = read(help_doc_location)
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)
        await send_message(help_message, interaction.followup.send)

    client.run(token)
