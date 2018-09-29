import os

HOST = os.getenv('APP_HOST', '0.0.0.0')
PORT = os.getenv('APP_PORT', '8350')

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', 'This is my secret')

    # Setting this variable ensure that flask restplus doc is enabled and
    # available at the url
    API_DOCS_URL = '/doc/'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    # Setting this variable to false disables the docs on production
    API_DOCS_URL = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
