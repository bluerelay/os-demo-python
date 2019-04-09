from sanic.response import json

async def hello(request):
    msg = 'hello world'
    return json({'message': msg})

async def health(request):
    return json({'success': True})