import os
import discord
from discord.ui import Button, View

from src.modal import ModalSample
from src.button import modal_button

from utils.fileio import read
from utils.message import send

# ty design pattern class


class Bot(discord.Client):
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

        self.register_cogs()
        self.synced = False

    def register_cogs(self):
        self.event(self.on_message)
        self.tree.command(
            name="help",
            description="use guide"
        )(self.help)
        self.tree.command(
            name="modal",
            description="testing modals"
        )(self.modal)

    async def on_ready(self):

        # Replace GUILD_ID with the actual guild ID
        guild = discord.Object(id=os.getenv("TESTING_GUILD_ID"))
        await self.tree.sync(guild=guild)
        print(
            f"Logged in as {self.user} and synced commands to guild ID {guild.id}")

        # sync commands if not already done
        if not self.synced:
            await self.tree.sync()
            self.synced = True

    async def on_message(self, message: discord.Message):
        # skip slash commands and self
        if message.type is discord.MessageType.chat_input_command:
            return
        if message.author == self.user:  # must use ==, not 'is'
            return

        # flags to identify source of message
        is_dm = not message.guild
        is_mentioned = self.user in message.mentions
        # flag to identify if message is a reply
        if message.reference:
            # type: discord.Message
            msg_replied = await message.channel.fetch_message(message.reference.message_id)

        # sample usage of buttons/modals
        if is_mentioned:
            await message.channel.send(
                "Click the button below!",
                view=await modal_button()
            )

    async def help(self, interaction: discord.Interaction):
        # this should be relative to root directory
        help_doc_location = "assets/docs/help.md"
        help_message = read(help_doc_location)
        # ephemeral=True means hidden reply
        await interaction.response.defer(ephemeral=False)
        await send(help_message, callback=interaction.followup.send)

    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ModalSample())

    @staticmethod
    def get_cmd_header(
        id: int,
        title: str
    ) -> str:
        return f'> **{title}** - <@{str(id)}> \n\n'
