import os

from werkzeug.middleware.proxy_fix import ProxyFix

from sample_project.app import create_app


config_name = os.getenv('APP_SETTINGS', 'development')
app = create_app(config_name)


# You only need ProxyFix if your app is deployed behind an ELB.
# It adds the `Forwarded` headers
app.wsgi_app = ProxyFix(app.wsgi_app)
