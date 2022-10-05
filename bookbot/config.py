from environs import Env

# Создаем класс Config с полями token и admin_ids
class Config:
    def __init__(self, token: str, admin_ids: list[int]) -> None:
        self.token = token
        self.admin_ids = admin_ids


# Создаем функцию, которая будет читать файл .env возвращать экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(token=env.str('BOT_TOKEN'),
                  admin_ids=list(map(int, env.list('ADMIN_IDS'))))