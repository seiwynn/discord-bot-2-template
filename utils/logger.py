import logging
from logging import handlers
import os

# if you want super verbose logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{'
)

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
file_handler = handlers.RotatingFileHandler(
    filename='logs/discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=2,
)
file_handler.setFormatter(formatter)

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logging.getLogger('discord').addHandler(console_handler)

logger.addHandler(file_handler)
