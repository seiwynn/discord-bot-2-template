from discord import Message, Interaction
from typing import Union
from utils import msg_split


async def send_message(
    outgoing_msg_content: str,
    incoming_msg_obj: Union[Message, Interaction]
) -> None:
    # split message into segments
    segments = msg_split.split_message(outgoing_msg_content)

    # discord allows multiple followups, so we can use only followups
    while segments:
        segment = segments.pop(0)

        if isinstance(incoming_msg_obj, Interaction):
            # slash commands
            await incoming_msg_obj.followup.send(segment)
        else:
            # normal messages
            await incoming_msg_obj.channel.send(segment)


def get_cmd_header(
    id: int,
    title: str
) -> str:
    return f'> **{title}** - <@{str(id)}> \n\n'
