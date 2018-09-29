import json

from sample_project.tests.conftest import AppTestCase


class PersonTestCase(AppTestCase):
    url = 'sample_project/api/v1.0/persons'

    def test_create_person(self):
        resp = self.client.post(
            self.url,
            data=json.dumps({
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_person_not_found(self):
        resp = self.client.get(self.url + '/10')
        self.assertEqual(resp.status_code, 404)

    def test_get_person(self):
        resp_create = self.client.post(
            self.url,
            data=json.dumps({
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }), content_type='application/json')

        resp = self.client.get(
            '{}/{}'.format(self.url, resp_create.json['person']['id'])
        )
        self.assertEqual(resp.status_code, 200)
