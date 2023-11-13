from discord import Message, InteractionType

from utils import message_utils


async def send_message(
    outgoing_msg_content: str,
    incoming_msg_obj: Message
) -> None:
    # split message into segments
    segments = message_utils.split_message(outgoing_msg_content)

    # discord allows multiple followups, so we can use only followups
    while segments:
        segment = segments.pop(0)

        if incoming_msg_obj.type is not InteractionType.application_command:
            await incoming_msg_obj.channel.send(segment)
        else:
            await incoming_msg_obj.followup.send(segment)
