import json

from tests.views import TCBase


class TestAccount(TCBase):
    def testA_signup(self):
        res = self.client.post(
            '/signup',
            data=json.dumps({'id': 'new', 'pw': 'test', 'name': 'test'}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)

        # Already existing id
        res = self.client.post(
            '/signup',
            data=json.dumps({'id': 'new', 'pw': 'test', 'name': 'test'}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 204)

    def testB_auth(self):
        # Success
        res = self.client.post(
            '/auth',
            data=json.dumps({'id': 'test', 'pw': 'test'}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data.decode())
        self.assertTrue('accessToken' in data)
        self.assertTrue('refreshToken' in data)

        # Incorrect id/pw
        res = self.client.post(
            '/auth',
            data=json.dumps({'id': 'dd', 'pw': 'dd'}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def testC_refresh(self):
        res = self.client.get(
            '/refresh',
            headers={'Authorization': self.refresh_token}
        )
        self.assertEqual(res.status_code, 200)

        self.assertTrue('accessToken' in json.loads(res.data.decode()))
