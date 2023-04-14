from . import sqlite_logic
from modules.utils import main_config

db = sqlite_logic.DataBase(main_config.bot.main_db)