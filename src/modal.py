import discord


class ModalSample(discord.ui.Modal):
    def __init__(self):
        super().__init__(
            title="Form example",
            timeout=300,
            custom_id="modal_sample"
        )

        # Instance attributes for text inputs
        self.s_short = discord.ui.TextInput(
            custom_id='short_sample',
            label='Short text',
            placeholder='one line of text...',
            required=False
        )

        self.s_long = discord.ui.TextInput(
            custom_id='long_sample',
            label='Long text',
            style=discord.TextStyle.long,
            placeholder='this can take multiple lines of text...',
            required=False,
            max_length=500,
        )

        # Add items to the modal
        self.add_item(self.s_short)
        self.add_item(self.s_long)

    async def on_submit(self, interaction: discord.Interaction):
        # Handling the submission of the modal
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(
            f'You submitted: {self.s_short.value}\nand...\n{self.s_long.value}!', ephemeral=True
        )
