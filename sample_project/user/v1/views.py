from flask_restx import Resource, fields
from flask import request

from sample_project.user import ns


user = ns.model('User', {
    'id': fields.Integer,
    'name': fields.String(required=True, min_length=1),
    'email': fields.String(required=True, min_length=5),
})


@ns.route('/users', methods=['POST'])
class User(Resource):

    @ns.expect(user, validate=True)
    @ns.marshal_with(user, envelope='user')
    def post(self):
        data = request.json
        data['id'] = 1
        return data, 201


@ns.route('/users/<string:user_id>', methods=['GET'])
class UserDetail(Resource):
    @ns.marshal_with(user, envelope='user')
    def get(self, user_id):
        if user_id == '1':
            return {
                'id': 1,
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }
        return {}, 404
