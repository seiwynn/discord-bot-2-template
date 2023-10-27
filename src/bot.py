import os
import asyncio
import discord
from src.async_client import AsyncClient

# this should be the only actual discord client existing.
# it will be connected to discord in run_discord_bot().
client = AsyncClient()

def run_discord_bot():
    
    @client.event
    async def on_message(message):
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

        # https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working
        # but apparently we don't need this anymore?
        # await client.process_commands(message)

    @client.tree.command(name="check-status", description="Check most recent status of a human - Hitomi included.")
    async def check_status(interaction: discord.Interaction, *, member: discord.Member = None):
        # await interaction.response.send_message(f"Most recent update from {member.name}: ")
        if not member:
            member = interaction.user
        if not check_recorded_user(member):
            await interaction.response.send_message(f"{member.name} has not been recorded.")
            return
        # TODO: get member status from data storage
        # message link: https://discord.com/channels/server_id/channel_id/message_id
        pass

    @client.tree.command(name="update", description="Grab your most recent messages in this channel as a new update.")
    async def update_status(interaction: discord.Interaction):
        if not check_recorded_user(interaction.user):
            await interaction.response.send_message(f"Hmmm... you're not one of the humans allowed to store data. \nPlease contact miss Hitomi, as she hasn't taught me how to add humans to the list yet.")
        # TODO: get recent messages from channel
        # TODO: pick out messages from user who called this command
        # TODO: limit to messages from the last 1 hour
        # TODO: store messages in data storage
        pass

    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client.run(TOKEN)

def check_recorded_user(member: discord.Member) -> bool:
    # TODO: check if member is human
    # TODO: check if member is one of the humans allowed to store data
    pass
