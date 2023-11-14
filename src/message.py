from discord import Message, Interaction, InteractionType
from typing import Union
from utils.msg_split import split_message


async def send_message(
    outgoing_msg_content: str,
    incoming_msg_obj: Union[Message, Interaction]
) -> None:
    # split message into segments
    segments = split_message(outgoing_msg_content)

    # discord allows multiple followups, so we can use only followups
    while segments:
        segment = segments.pop(0)

        if incoming_msg_obj.type is InteractionType.application_command:
            await incoming_msg_obj.followup.send(segment)
        else:
            # not a slash command
            # most likely a regular message
            await incoming_msg_obj.channel.send(segment)
            

def get_cmd_header(
    id: int, 
    title: str
) -> str:
    return f'> **{title}** - <@{str(id)}> \n\n'
