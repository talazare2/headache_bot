from environs import Env
from dataclasses import dataclass



@dataclass
class TgBot:
    token: str            # TG access token
#    admin_ids: list[int]  # List of admins id (not used in the project for now)


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str) -> Config:

    env: Env = Env()
    env.read_env(path)

    print('BOT_TOKEN:', env)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))