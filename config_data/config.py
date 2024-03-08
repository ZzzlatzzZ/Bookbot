from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]    # Список id администраторов

@dataclass
class Config:
    tgbot: TgBot

# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: "str | None" = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tgbot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        )
    )