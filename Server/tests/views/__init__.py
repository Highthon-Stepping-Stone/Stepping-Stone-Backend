from unittest import TestCase as TC
import json

from werkzeug.security import generate_password_hash

from app import app
from app.models.account import AccountModel


class TCBase(TC):
    def __init__(self, *args, **kwargs):
        TC.__init__(self, *args, **kwargs)

        self.client = app.test_client()
        self.id = 'test'
        self.pw = 'test'
        self.hashed_pw = generate_password_hash(self.pw)

    def _create_fake_accounts(self):
        AccountModel(
            id=self.id,
            pw=self.hashed_pw,
            name='test'
        ).save()

    def _auth(self, auth_url_rule):
        res = self.client.post(
            auth_url_rule,
            data=json.dumps({'id': self.id, 'pw': self.pw}),
            content_type='application/json'
        )

        return json.loads(res.data.decode())

    def _get_access_token(self, auth_url_rule='/auth'):
        resp = self._auth(auth_url_rule)

        return 'JWT ' + resp['accessToken']

    def _get_refresh_token(self, auth_url_rule='/auth'):
        resp = self._auth(auth_url_rule)

        return 'JWT ' + resp['refreshToken']

    def setUp(self):
        self._create_fake_accounts()
        self.access_token = self._get_access_token()
        self.refresh_token = self._get_refresh_token()

    def tearDown(self):
        AccountModel.objects.delete()
        # 마이그레이션 해야함
