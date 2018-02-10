from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.docs.account.signup import *
from app.models.account import AccountBase, ServiceAccountModel
from app.models.school import SchoolModel
from app.views import BaseResource, auth_required, json_required

api = Api(Blueprint('account-signup-api', __name__))


@api.resource('/signup')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    @json_required
    def post(self):
        """
        서비스 자체 회원가입
        """
        id = request.json['id']
        pw = request.json['pw']

        hashed_pw = generate_password_hash(pw)

        if ServiceAccountModel.objects(id=id).first():
            return Response('', 204)

        ServiceAccountModel(
            id=id,
            pw=hashed_pw
        ).save()


@api.resource('/additional-info')
class AdditionalInfo(BaseResource):
    @swag_from(ADDITIONAL_INFO_POST)
    @auth_required
    @json_required
    def post(self):
        """
        사용자 추가 정보 입력
        """
        school_id = request.json['schoolId']
        grade = request.json['grade']
        class_ = request.json['class']
        admission_year = request.json['admissionYear']

        if len(school_id) != 24:
            return Response('', 204)

        school = SchoolModel.objects(id=school_id).first()
        if not school:
            return Response('', 204)

        user = AccountBase.objects(id=get_jwt_identity()).first()

        user.update(
            school_id=school.id,
            grade=grade,
            class_=class_,
            admission_year=admission_year
        )

        return Response('', 201)
