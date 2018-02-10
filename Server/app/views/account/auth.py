from uuid import uuid4

from flask import Blueprint, Response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api, request
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.docs.account.auth import *
from app.models.account import ServiceAccountModel, SNSAccountModel, RefreshTokenModel
from app.views import BaseResource, json_required

api = Api(Blueprint('account-auth-api', __name__))


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH_POST)
    @json_required
    def post(self):
        """
        서비스 자체 계정 로그인
        """
        id = request.json['id']
        pw = request.json['pw']

        hashed_pw = generate_password_hash(pw)
        user = ServiceAccountModel.objects(id=id, pw=hashed_pw).first()

        if not user:
            return Response('', 401)

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=user,
            pw_snapshot=pw
        ).save()
        # Generate new refresh token made up of uuid4

        return {
            'accessToken': create_access_token(id),
            'refreshToken': create_refresh_token(str(refresh_token))
        }, 200


@api.resource('/auth/sns')
class SNSAuth(BaseResource):
    @swag_from(SNS_AUTH_POST)
    @json_required
    def post(self):
        """
        SNS 계정으로 로그인
        """
        id = request.json['id']
        connected_service = request.json['connected_service']

        user = SNSAccountModel.objects(id=id).first()
        if not user:
            user = SNSAccountModel(
                id=id,
                connected_service=connected_service
            ).save()

            status_code = 201
        else:
            status_code = 200

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=user
        ).save()
        # Generate new refresh token made up of uuid4

        return {
            'accessToken': create_access_token(id),
            'refreshToken': create_refresh_token(str(refresh_token))
        }, status_code


@api.resource('/refresh')
class Refresh(BaseResource):
    @swag_from(REFRESH_GET)
    @jwt_refresh_token_required
    def get(self):
        """
        새로운 Access Token 획득
        """
        token = RefreshTokenModel.objects(token=get_jwt_identity()).first()

        if not token or token.token_owner.pw != token.pw_snapshot:
            # Invalid token or the token issuing password is different from the current password
            # Returns status code 205 : Reset Content
            return Response('', 205)

        return {
            'accessToken': create_access_token(token.token_owner.id)
        }, 200
