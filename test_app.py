import unittest
import json
import app

BASE_URL = 'http://localhost:5000/users'

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
    #
    # def tearDown(self):
    #     super(test_create_user(), self).tearDown()

    def test_get_all_users(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 16)

    def test_get_one_user(self):
        response = self.app.get('http://localhost:5000/users/14')
        data = json.loads(response.get_data())

        self.assertEqual(data['email'], 'gregory@example.com')
        self.assertEqual(data['first_name'], 'Gregory')
        self.assertEqual(data['last_name'], 'Anderson')
        self.assertEqual(data['phone_number'], 1234567890)
        self.assertIsNotNone(data['password'])
        self.assertEqual(data['role'], 'volunteer')

    def test_get_one_user_sad_path(self): #leaves field out
        response = self.app.get('http://localhost:5000/users/1004')
        data = json.loads(response.get_data())
        # import ipdb; ipdb.set_trace()

        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in data)
        self.assertTrue('message' in data)
        self.assertEqual(data['error'], 'Bad Request')
        self.assertEqual(data['message'], 'User does not exist')

    def test_user_not_created(self):
        body = {}
        response = self.app.post('http://localhost:5000/user', data=json.dumps(body), content_type='application/json')
        data = json.loads(response.get_data())

        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in data)
        self.assertTrue('message' in data)
        self.assertEqual(data['error'], 'Bad Request')
        self.assertEqual(data['message'], 'Error: Missing Fields')

    def test_user_update_user(self):
        body = {'first_name': 'Taylor James', 'last_name': 'deherrera', 'email': 'tayd051693@example.com', 'password': 'password', 'phone_number': 1234567890}
        request = self.app.put('http://localhost:5000/users/2', data=json.dumps(body), content_type='application/json')

        response = self.app.get('http://localhost:5000/users/2')
        data_2 = json.loads(response.get_data())

        # import ipdb; ipdb.set_trace()

        self.assertEqual(request.status_code, 204)
        self.assertEqual(data_2['first_name'], 'Taylor James')

    def test_user_not_updated(self):
        body = {}
        response = self.app.put('http://localhost:5000/users/2', data=json.dumps(body), content_type='application/json')

        data = json.loads(response.get_data())

        self.assertEqual(response.status_code, 400)

        self.assertTrue('error' in data)
        self.assertTrue('message' in data)
        self.assertEqual(data['error'], 'Bad Request')
        self.assertEqual(data['message'], 'Error: Missing Fields')



    @unittest.skip('skip')
    def test_user_deleted(self):
        request = self.app.delete('http://localhost:5000/users/17')

        self.assertEqual(request.status_code, 204)
        
    def test_create_user(self):
        body = {'first_name': 'tay', 'last_name': 'deherrera', 'email': 'tayd0593@example.com', 'password': 'password', 'phone_number': 1234567890, 'role': 'volunteer'}
        response = self.app.post('http://localhost:5000/user', data=json.dumps(body), content_type='application/json')
        data = json.loads(response.get_data())

        self.assertEqual(response.status_code, 201)
        # self.assertIsInstance(data, User)
        # import ipdb; ipdb.set_trace()
