import os

from sanic import Blueprint
import pusher


class PushService:
    """provides pusher service"""
    client = None

    @classmethod
    def init_client(cls, config):
        cls.client = pusher.Pusher(**config)

    def __init__(self, socket_id=None, channel='redhat-demo'):
        self.socket_id = socket_id
        self.channel = channel
    
    def trigger(self, event_name, data):
        self.client.trigger(self.channel, event_name, data, socket_id=self.socket_id)


pushBp = Blueprint(name='push_service')
@pushBp.listener('before_server_start')
def start_pusher(app, loop):
    PushService.init_client({
        'app_id': os.getenv('PUSHER_ID'),
        'key': '99aa5a832d330c77e5a3',
        'secret': os.getenv('PUSHER_SECRET'),
        'cluster': 'us2',
        'ssl': True
    })