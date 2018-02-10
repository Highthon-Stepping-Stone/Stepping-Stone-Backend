import json

from app.models.album import ScheduledAlbumModel, ScheduledFolderModel
from tests.views import TCBase


class TestAlbum(TCBase):
    def tearDown(self):
        ScheduledAlbumModel.objects.delete()
        TCBase.tearDown(self)

    def testA_scheduledAlbum(self):
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

        # Signup school
        res = self.client.post(
            '/signup/school',
            data=json.dumps({'schoolId': school_id, 'admissionYear': 2018}),
            headers={'Authorization': self.access_token},
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)

        res = self.client.get(
            '/album/scheduled',
            headers={'Authorization': self.access_token}
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data.decode())

    def testB_freeAlbum(self):
        pass
