from sanic import Blueprint

import apis


routes = Blueprint('routes')
routes.add_route(handler=apis.hello, uri='/hello', methods=['GET'])
