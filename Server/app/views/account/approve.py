from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.account.approve import *
from app.models.account import AccountModel
from app.views import BaseResource

api = Api(Blueprint('account-approve-api', __name__))


@api.resource('/signup/approve/list')
class ApproveSignupList(BaseResource):
    @swag_from(APPROVE_SIGNUP_LIST_POST)
    def post(self):
        """
        가입 승인 요청자 목록 조회
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()

        if not user.is_admin:
            abort(403)

        return self.unicode_safe_json_response([{
            'id': user.id,
            'name': user.name,
            'admissionYear': user.admission_year
        } for user in AccountModel.objects(accepted=False, school=user.school)])


@api.resource('/signup/approve')
class ApproveSignup(BaseResource):
    @swag_from(APPROVE_SIGNUP_POST)
    def post(self):
        """
        가입 요청 승인
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()

        if not user.is_admin:
            abort(403)

        id = request.json['id']

        user = AccountModel.objects(id=id).first()
        if not user:
            return Response('', 204)

        user.update(signed=True)

        return Response('', 200)

    @swag_from(APPROVE_SIGNUP_DELETE)
    def delete(self):
        """
        가입 요청 거절
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()

        if not user.is_admin:
            abort(403)

        id = request.json['id']

        user = AccountModel.objects(id=id).first()
        if not user:
            return Response('', 204)

        user.update(signed=False)

        return Response('', 200)
