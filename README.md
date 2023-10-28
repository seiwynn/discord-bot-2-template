# discord-bot-2-mystatus
So that you know what I'm up to.

<!-- ### How to use -->

<!-- TODO maybe I should write this? -->
<!-- (later) -->

### TODOs
- actual logger
  - no, print stmtys won't work
- status update function
  - /status
  - /update, which grabs history messages
    - ~~might also record future messages for 1 hour~~
    nah that would require a ton of event listening 
  - use specific emoji to ask bot to update
    - probably a custom emoji?
    - ~~:sacabam-update:~~
    - special response, e.g. private msg/card
  - /clear

- other utils ~~that might take too much time and I want quick stuff now~~
  - message splitter for 2000 char limit
  - message queue for slowmode/awaits
    - 3rd party api requests / scraping / file io


### Credits

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Random GPT bot that I used as my 1st bot template](https://github.com/Zero6992/chatGPT-discord-bot)
  - ~~Definitely not because I learned 90% of my python from existing repos' copypasta.~~
