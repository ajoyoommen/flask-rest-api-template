from flask import Flask

from flask_restx.apidoc import apidoc


ROOT_URL = '/sample_project'


def create_app(config_name):
    from sample_project.config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["APPLICATION_ROOT"] = ROOT_URL

    # Flask restplus uses apidoc to generate URLs for static files in swagger.
    #
    # If any of the follwing is true:
    #   1. apidoc is not registered as a blueprint (default use case)
    #   2. apidoc is registered after another blueprint,
    # restplus auto-registers the default apidoc at '/'.
    #
    # Hence, the `apidoc` should be the first blueprint registered. And it is
    # mounted at ROOT_URL
    app.register_blueprint(apidoc, url_prefix=ROOT_URL)

    with app.app_context():
        from sample_project.api_v1 import blueprint as api
        from sample_project.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL + '/api/v1.0')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')
    return app
