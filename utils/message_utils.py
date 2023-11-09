import re
from discord import Message, InteractionType

async def send_message(outgoing_msg_content: str, incoming_msg_obj: Message) -> None:
    pass
    # if (message.type is not InteractionType.application_command) or has_followed_up:
    #     await message.channel.send(response)
    # else:
    #     await message.followup.send(response)
    #     has_followed_up = True

    # return has_followed_up

async def split_message(content: str) -> list[str]:
    char_limit = 1500
    if len(content) <= char_limit:
        return [content]
    
    # TODO: deal with sequences of ```` (4 or more) in the message, replece with \`
    # too many `s screw up markdown, even in code blocks
    # typora has its own way of dealing with this, but not discord.

    # TODO: code block separation and internal splitting
    # TODO: deal with rest of the text, try to split on whitespace
    