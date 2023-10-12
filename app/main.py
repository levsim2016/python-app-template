#!/usr/bin/python3
from app.config import Config

config = Config()


def run():
    # Replace by your code
    print('\033[92m' + '\nStart coding! \n')
    print('\033[93m' + 'Environment variables from .env:')
    print(Config())


if __name__ == '__main__':
    run()
