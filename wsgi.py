from sanic import Sanic

from routes import routes
from psql import psql


application = Sanic('os-demo-python')
application.blueprint(routes)
application.blueprint(psql)