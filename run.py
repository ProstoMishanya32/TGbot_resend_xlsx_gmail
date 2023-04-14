# - *- coding: utf- 8 - *-
from aiogram import executor, Dispatcher

from modules import alerts
from modules.utils import main_config, bot_commands
from modules.utils.logging_system import logger
from modules.services import db, gmail_logic

from handlers import dp

from threading import Thread, Lock
import os, sys, colorama, asyncio



colorama.init()

# запуск бота

async def on_startup(dp: Dispatcher):
    asyncio.create_task(gmail_logic.send_gmail())

    db.start_bot(colorama)
    await bot_commands.set_commands(dp)
    await alerts.on_startup_notify(dp)
    logger.warning("Бот вошел в сеть")
    print(colorama.Fore.LIGHTBLUE_EX + "--- Бот вошел в сеть ---\n" + colorama.Fore.LIGHTRED_EX +
    "--- Разработчик @michailcoding ---\n"
    + colorama.Fore.YELLOW + "--- https://kwork.ru/user/prostomishanya32 ---" +  colorama.Fore.RESET)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
