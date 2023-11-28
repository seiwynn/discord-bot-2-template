import re


def get_min_len(): return 1500
def get_max_len(): return 1800


async def send(
    outgoing_msg_content: str,
    callback,
    *,
    first_msg_callback=None
) -> None:
    # split message into segments
    segments = split_message(outgoing_msg_content)
    # if you want to deal with the first segment differently
    if first_msg_callback:
        await first_msg_callback(segments[0])
        segments.pop(0)

    # everything else
    while segments:
        segment = segments.pop(0)
        await callback(segment)


def split_message(content: str) -> list[str]:
    if len(content) <= get_max_len():
        return [content]

    # tyvm chatGPT
    four_backtick_pattern = r'`{4,}'
    code_block_pattern = r'^(?P<text>[\s\S]*?)```(?P<lang>\w+)?(?P<code>[\s\S]*?)```'

    # Handle sequences of four or more backticks in the message
    # Replace each occurrence with a string of backslashes and backticks
    content = re.sub(
        pattern=four_backtick_pattern,
        repl=lambda match: r'\`' * len(match.group(0)),
        string=content
    )

    segments = []

    # handle mixed code blocks and text
    match = re.match(code_block_pattern, content)
    while match:
        # in case text is nothing but whitespace
        text = match.group('text').strip()
        if text:
            text_segments = split_smart(text)
            segments.extend(text_segments)

        code_block = match.group('code').strip()
        language = match.group('lang') or ''
        code_segments = split_code(code=code_block, lang=language)
        segments.extend(code_segments)

        # remove matched text+code
        content = content[match.end():].lstrip()

        # check for more code blocks
        match = re.match(code_block_pattern, content)

    # handle remaining text
    text_segments = split_smart(content)
    segments.extend(text_segments)

    return segments


def split_code(code: str, lang: str) -> list[str]:
    code_header = f'```{lang}\n'
    code_footer = '\n```'
    # skip short code blocks
    if len(code) <= get_max_len()-len(code_header)-len(code_footer):
        return [code_header + code + code_footer]

    # split code by newlines, instead of whitespace
    segments = split_smart(
        code,
        pattern=r'\n\s*\S',
        local_min=get_min_len()-len(code_header)-len(code_footer),
        local_max=get_max_len()-len(code_header)-len(code_footer)
    )

    # add code block header and footer
    segments = [code_header + segment + code_footer for segment in segments]
    return segments


def split_smart(
    text: str,
    pattern: str = r'\s\S',
    local_min=get_min_len(),
    local_max=get_max_len()
) -> list[str]:

    segments = []
    while text:
        text = text.strip()

        # If the remaining text is shorter than the max length, add it as is
        if text and len(text) <= local_max:
            segments.append(text)
            break

        # Find first group of whitespace in [local_min, local_max]
        split_index = local_max
        match = re.search(pattern, text[local_min:local_max])
        if match:
            # split before next word
            # e.g. 'hello   world' -> split at ' w'
            split_index = local_min + match.start() + 1

        # Add the segment and remove it from the text
        segments.append(text[:split_index].strip())
        text = text[split_index:]

    return segments
