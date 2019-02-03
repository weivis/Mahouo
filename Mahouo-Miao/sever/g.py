from gevent.wsgi import WSGIServer
from app import app, blueprint

http_server = WSGIServer(('127.0.0.1', 8401), app)
http_server.serve_forever()