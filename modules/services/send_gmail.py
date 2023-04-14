# - *- coding: utf- 8 - *-
from modules.utils import main_config

from bot_telegram import bot


async def send_gmail_in_channel(file_id):
    print("идет отправка")
    await bot.send_document(main_config.bot.channel_id, file_id)