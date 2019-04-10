from sanic import Blueprint
from sanic.exceptions import NotFound
from sanic.response import file

import apis


routes = Blueprint('routes')
routes.add_route(handler=apis.get_messages, uri='/messages', methods=['GET'])
routes.add_route(handler=apis.save_message, uri='/message', methods=['POST'])
routes.add_route(handler=apis.health, uri='/health', methods=['GET'])
# ui
routes.static('/', './ui/dist', name='ui')
routes.static('/', './ui/dist/index.html', name='index')
@routes.exception(NotFound)
async def handleNotFound(request, exception):
    return await file('./ui/dist/index.html')
