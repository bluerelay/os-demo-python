from sanic.response import json

async def hello(request):
    msg = 'hello world'
    return json({'message': msg})