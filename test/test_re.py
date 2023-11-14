import re
four_backtick_pattern = r'`{4,}'

content = "``````````````````"

content = re.sub(
    pattern=four_backtick_pattern,
    # repl=replace_backticks,
    repl=lambda match: r"\`" * len(match.group(0)),
    string=content
)

print(content)

s = "\n\n\n"
print(len(s))

