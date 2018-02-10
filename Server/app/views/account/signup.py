from flask import Blueprint, Response
from flask_restful import Api, current_app, request
from flasgger import swag_from

from app.docs.account.signup import *
from app.views import BaseResource, auth_required, json_required

api = Api(Blueprint('account-signup-api', __name__))


class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    @json_required
    def post(self):
        """
        서비스 자체 회원가입
        """


class AdditionalInfo(BaseResource):
    @swag_from(ADDITIONAL_INFO_POST)
    @json_required
    def post(self):
        """
        사용자 추가 정보 입력
        """

