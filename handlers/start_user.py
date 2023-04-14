# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ContentType, ChatType
from aiogram.utils.exceptions import MessageCantBeDeleted
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import hlink
from aiogram.utils.deep_linking import get_start_link, decode_payload

from modules.utils import main_config

from contextlib import suppress
from bot_telegram import dp
from datetime import datetime

import random, os, asyncio

from bot_telegram import bot


@dp.message_handler(commands = ['start'], state = "*")
async def start(message: Message, state: FSMContext, priglacili = False):
    await message.answer("<b>Привет, это бот для отправки с GMAIL почты файлов в канал</b>")
