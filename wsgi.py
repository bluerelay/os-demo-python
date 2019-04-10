from sanic import Sanic

from routes import routes
from psql import psql
from push_service import pushBp


application = Sanic('os-demo-python')
application.blueprint(routes)
application.blueprint(psql)
application.blueprint(pushBp)