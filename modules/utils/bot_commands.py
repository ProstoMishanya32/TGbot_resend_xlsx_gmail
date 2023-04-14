# - *- coding: utf- 8 - *-
from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from modules.services.json_logic import get_admins
from modules.utils import main_config


user_commands = [
    BotCommand("start", "♻ Перезапустить бота"),
]

admin_commands = [
    BotCommand("start", "♻ Перезапустить бота"),
    BotCommand("stop", "Остановить Бота"),
    BotCommand("admin_menu", "Админ меню")
]

# Установка команд
async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
    for admin in get_admins():
        try:
            await dp.bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))
        except:
            pass
    await dp.bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=main_config.bot.main_admin))
