from typing import Callable, Any
import inspect
from utils import msg_split


async def send_message(
    outgoing_msg_content: str,
    callback: Callable[[str], Any]
) -> None:
    # split message into segments
    segments = msg_split.split_message(outgoing_msg_content)

    # discord allows multiple followups, so we can use only followups
    while segments:
        segment = segments.pop(0)

        # this would be your own function that sends a message
        if inspect.iscoroutinefunction(callback):
            await callback(segment)
        else:
            # shouldn't happen in discord, but just in case
            callback(segment)


def get_cmd_header(
        id: int,
        title: str
) -> str:
    return f'> **{title}** - <@{str(id)}> \n\n'
