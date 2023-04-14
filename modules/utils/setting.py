from modules.utils.creater_config import CreatingConfig


class MainConfig(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/main_config.json')
        self.bot = self.Bot(config = self)
        self.gmail = self.GMAIL(config = self)

    class Bot:
        def __init__(self, config : CreatingConfig) -> None:
            self.token = config.config_field(key = 'token', layer = 'bot', default = 'Здесь ваш Telegram Токен')
            self.main_admin = config.config_field(key='main_admin', layer='bot', default='Самый главный Администатор')
            self.admins = config.config_field(key='admins', layer='bot', default=[])
            self.channel_id  = config.config_field(key='channel_id', layer='bot', default='ID канала, для отправки файлов с почты')
            self.main_db  = config.config_field(key='main_db', layer='bot', default='Путь к базе данных')
            self.logs =  config.config_field(key='logs', layer='bot', default='Путь к логам')
    class GMAIL:
        def __init__(self, config : CreatingConfig) -> None:
            self.client_file = config.config_field(key = 'main_patclient_fileh_logs', layer = 'gmail', default = 'Путь к файлу credentials.json')
            self.api_name = config.config_field(key='api_name', layer='gmail', default='gmail')
            self.api_version  = config.config_field(key='api_version', layer='gmail', default='v1')
            self.file_extension = config.config_field(key='file_extension', layer='gmail', default='.xlsx')

