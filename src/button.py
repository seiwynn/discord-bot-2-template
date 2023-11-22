import discord
from discord.ui import Button, View
from src.modal import ModalSample


async def modal_button():
    button = Button(label="Modal Sample", style=discord.ButtonStyle.primary)

    async def button_callback(interaction: discord.Interaction):
        await interaction.response.send_modal(ModalSample())
        await interaction.followup.send("Button clicked!", ephemeral=True)

    button.callback = button_callback
    view = View()
    view.add_item(button)

    return view
