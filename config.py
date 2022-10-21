import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
DB_ECHO = True
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_PORT = ''
DB_NAME = 'backstage'
SECRET = 'some_secret_key'
ALGORITHM = 'HS256'