from environs import Env

class Config():
    def __init__(self, token, admin_ids):
        self.token = token
        self.admin_ids = admin_ids


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(token=env.str('BOT_TOKEN'),
                  admin_ids=list(map(int, env.list('ADMIN_IDS'))))