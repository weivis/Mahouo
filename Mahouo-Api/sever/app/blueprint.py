from app import app
from app.apilist import apilist
from app.citygps import citygps

app.config['SERVER_NAME'] = 'mahouo.com'
app.register_blueprint(apilist, subdomain='api', url_prefix='/applist')
app.register_blueprint(citygps, subdomain='api', url_prefix='/gps')
#app.register_blueprint(user, subdomain='account', url_prefix='/user') #user