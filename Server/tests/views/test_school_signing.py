import json

from app.models.account import AccountModel, RefreshTokenModel
from tests.views import TCBase


class TestSchoolSignup(TCBase):
    def tearDown(self):
        AccountModel.objects.delete()
        RefreshTokenModel.objects.delete()

    def testA_schoolSignup(self):
        # Non-existing check
        res = self.client.get(
            '/signup/school',
            headers={'Authorization': self.access_token}
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data.decode())
        self.assertEqual(data['schoolName'], None)
        self.assertEqual(data['requested'], False)
        self.assertEqual(data['signed'], False)

        # Get random school id
        res = self.client.post(
            '/school',
            data=json.dumps({'keyword': '대덕'}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data.decode())
        self.assertTrue('schoolId' in data[0])
        school_id = data[0]['schoolId']
        school_name = data[0]['schoolName']

        # Signup school
        res = self.client.post(
            '/signup/school',
            data=json.dumps({'schoolId': school_id, 'admissionYear': 2018}),
            headers={'Authorization': self.access_token},
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)

        res = self.client.get(
            '/signup/school',
            headers={'Authorization': self.access_token}
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data.decode())
        self.assertEqual(data['schoolName'], school_name)
        self.assertEqual(data['requested'], True)
        self.assertEqual(data['signed'], True)
