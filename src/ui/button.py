import discord
from discord.ui import Button, View
from src.ui.modal import ModalSample


async def modal_button():
    button = Button(label="Modal Sample", style=discord.ButtonStyle.primary)

    async def button_callback(interaction: discord.Interaction):
        # modals can only be sent as a response
        # to a button/slash command interaction
        await interaction.response.send_modal(ModalSample())
        await interaction.followup.send("Button clicked!", ephemeral=True)

    button.callback = button_callback
    view = View()
    view.add_item(button)

    return view
