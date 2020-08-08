from flask import request
from flask_restx import Resource, fields

from sample_project.person import ns


person = ns.model('Person', {
    'id': fields.Integer,
    'name': fields.String(required=True, min_length=1),
    'email': fields.String(required=True, min_length=5),
})


@ns.route('/persons', methods=['POST'])
class Person(Resource):

    @ns.expect(person, validate=True)
    @ns.marshal_with(person, envelope='person')
    def post(self):
        data = request.json
        data['id'] = 1
        return data, 201


@ns.route('/persons/<string:person_id>', methods=['GET'])
class PersonDetail(Resource):
    @ns.marshal_with(person, envelope='person')
    def get(self, person_id):
        if person_id == '1':
            return {
                'id': 1,
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }
        return {}, 404
