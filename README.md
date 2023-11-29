# discord-bot-2-template
A template for my future bots.
Formerly [a status bot](https://github.com/seiwynn/discord-bot-4-shiro) - you'll notice older commits referring to that.

### Newly added features

- 11/13/2023: message splitter for 2000 char limit

### How to use

**You would need MESSAGE CONTENT INTENT in your bot page set as `ON`**

1. ~~I think I don't need to write this but still~~
    ```bash
    git clone
    cd discord-bot-2-template
    # python -m venv venv
    ```

2. Create a `.env` file in the root directory, `.env.example` is provided as a template.
    ```bash
    cp .env.example .env
    # modify .env as needed
    ```

3. Install dependencies and run:

    ```bash
    pip install -r requirements.txt
    python ./main.py
    ```

### TODOs
- ~~actual logger~~
- ~~message splitter for 2000 char limit~~
- message queue for slowmode/awaits
  - 3rd party api requests / scraping / file io


### Credits

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [discord.py official examples](https://github.com/Rapptz/discord.py/tree/master/examples)
- [Random GPT bot that I used as my 1st bot template](https://github.com/Zero6992/chatGPT-discord-bot)
- [python - How do i make a working slash command in discord.py - Stack Overflow](https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py)

~~probably will have even more copypasta from other bot templates/tutorials in the future~~