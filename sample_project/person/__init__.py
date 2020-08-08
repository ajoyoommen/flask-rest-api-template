from flask_restx import Namespace

ns = Namespace('Person', path='/')


from sample_project.person.v1 import views  # noqa
