from flask_restplus import Namespace

ns = Namespace('User', path='/')


from sample_project.user.v1 import views  # noqa
