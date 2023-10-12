import os
import pprint
import dotenv
from app.common.singleton import Singleton

ENV_FILENAME = '.env'


class Config(Singleton, dict):
    env_filepath: str = None
    _config: dict = None

    def __init__(self):
        super().__init__()
        if self._config is None:
            self._config = self._load_config()

        for (key, value) in self._config.items():
            self.__setitem__(key, value)

    def exists(self) -> bool:
        return self._config is not None

    def __str__(self):
        return pprint.pformat(self, indent=2, width=40)

    def _load_config(self) -> dict:
        pex_exec_filepath = os.environ.get('PEX')

        if pex_exec_filepath is not None:
            directory = os.path.dirname(pex_exec_filepath)
            env_filepath = os.path.join(directory, ENV_FILENAME)
        else:
            env_filepath = dotenv.find_dotenv(ENV_FILENAME)

        self.env_filepath = env_filepath

        return dotenv.dotenv_values(env_filepath)


if __name__ == '__main__':
    print(Config())
    print(Config().env_filepath)
