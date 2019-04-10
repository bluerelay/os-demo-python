from sanic.response import json


from psql import db
from push_service import PushService

async def get_messages(request):
    query = db.table('messages').select('author', 'content')
    messages = await query
    messages = [dict(m) for m in messages]
    return json(messages)

async def save_message(request):
    message = {
        'author': request.json['author'],
        'content': (request.json['content'][:2000] + '...') if len(request.json['content']) > 2000 else request.json['content']
    }
    await db.table('messages').insert(message)
    pusher = PushService(request.json['ping'])
    pusher.trigger('new-message', message)
    return json({'success': True, 'message': message})

async def health(request):
    return json({'success': True})