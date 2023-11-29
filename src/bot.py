import os
import discord
from discord import app_commands

from src.client import Client

# samples for ui stuff
from src.ui.modal import ModalSample
from src.ui.button import modal_button

from utils.logger import logger
from utils.fileio import read
from utils.message import send


def get_cli_with_cogs(token: str) -> discord.Client:
    client = Client(token=token)

    @client.event
    async def on_ready():
        # Replace GUILD_ID with the actual guild ID
        guild = discord.Object(id=os.getenv("TESTING_GUILD_ID"))
        await client.tree.sync(guild=guild)
        logger.info(
            f"Logged in as {client.user} and synced commands to guild ID {guild.id}"
        )
        client.current_channel = int(guild.id)

        # this will sync, but slower
        await client.tree.sync()

    @client.event
    async def on_message(message: discord.Message):
        # skip slash commands and self (and other bots)
        if message.type is discord.MessageType.chat_input_command:
            return
        if (message.author == client.user) or message.author.bot:  # must use ==, not 'is'
            return

        # flags to identify source of message
        is_dm = not message.guild
        is_mentioned = client.user in message.mentions
        if message.reference:
            # type: discord.Message
            msg_replied = await message.channel.fetch_message(message.reference.message_id)

    @client.tree.command(
        name="help",
        description="use guide"
    )
    async def help(interaction: discord.Interaction):
        # this should be relative to root directory
        help_doc_location = "assets/docs/help.md"
        help_message = read(help_doc_location)
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)
        await send(help_message, callback=interaction.followup.send)

    @client.tree.command(
        name="modal",
        description="modal sample"
    )
    async def modal(interaction: discord.Interaction):
        await interaction.response.send_modal(ModalSample())

    @client.tree.command(
        name="button",
        description="button sample"
    )
    async def button(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(
            "Click the button below!",
            view=await modal_button()
        )

    # stolen from https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
    @client.tree.command(
        name="echo",
        description="reiterate"
    )
    @app_commands.rename(echo_text="content")
    @app_commands.describe(echo_text="I'll repeat this!")
    @app_commands.choices(whisper=[
        app_commands.Choice(name="on", value="on"),
        app_commands.Choice(name="off", value="off")
    ])
    async def echo(interaction: discord.Interaction, *, echo_text: str, whisper: str = "off"):

        # ephemeral=True means hidden reply
        ep_flag = False
        # Additional logic based on the 'whisper' value
        if whisper == "on":
            # Handle the whisper "on" case
            ep_flag = True

        await interaction.response.defer(ephemeral=ep_flag)
        await interaction.followup.send(
            client.get_cmd_header(
                id=interaction.user.id,
                title="Echo"
            ) +
            f"Echoing: \n{echo_text}",
            ephemeral=ep_flag
        )

    return client
