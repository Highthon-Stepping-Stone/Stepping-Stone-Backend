from flask import Blueprint, Response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api, current_app, request
from flasgger import swag_from

from app.docs.account.auth import *
from app.models.account import ServiceAccountModel, SNSAccountModel, RefreshTokenModel
from app.views import BaseResource, auth_required, json_required

api = Api(Blueprint('account-auth-api', __name__))


class Auth(BaseResource):
    @swag_from(AUTH_POST)
    @json_required
    def post(self):
        """
        서비스 자체 계정 로그인
        """


class SNSAuth(BaseResource):
    @swag_from(SNS_AUTH_POST)
    @json_required
    def post(self):
        """
        SNS 계정으로 로그인
        """


class Refresh(BaseResource):
    @swag_from(REFRESH_GET)
    @jwt_refresh_token_required
    def get(self):
        """
        JWT Token refresh
        """

