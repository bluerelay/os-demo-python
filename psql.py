import asyncio
import os

from sanic import Blueprint
from windyquery import DB


db = DB()

psql = Blueprint(name='psql')

@psql.listener('before_server_start')
def start_db(app, loop):
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')
    asyncio.get_event_loop().run_until_complete(db.connect(os.getenv('DATABASE_NAME'), {
        'host': os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'port': os.getenv('{}_SERVICE_PORT'.format(service_name)),
        'database': os.getenv('DATABASE_NAME'),
        'username': os.getenv('DATABASE_USER'),
        'password': os.getenv('DATABASE_PASSWORD'),
    }, default=True))

@psql.listener('after_server_stop')
def stop_db(app, loop):
    asyncio.get_event_loop().run_until_complete(db.stop())