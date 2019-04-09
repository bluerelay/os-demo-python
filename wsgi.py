from sanic import Sanic

from routes import routes


application = Sanic('os-demo-python')
application.blueprint(routes)