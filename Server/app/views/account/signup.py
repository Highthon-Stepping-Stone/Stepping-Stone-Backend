from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.docs.account.signup import *
from app.models.account import AccountModel
from app.models.school import SchoolModel
from app.views import BaseResource, auth_required, json_required

# from utils import school_parser

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
        name = request.json['name']

        hashed_pw = generate_password_hash(pw)

        if AccountModel.objects(id=id).first():
            return Response('', 204)

        AccountModel(
            id=id,
            pw=hashed_pw,
            name=name
        ).save()

        return Response('', 201)


@api.resource('/signup/school')
class SchoolSignup(BaseResource):
    @swag_from(SCHOOL_SIGNUP_POST)
    @auth_required
    @json_required
    def post(self):
        """
        학교에 가입 요청
        """
        school_id = request.json['schoolId']
        admission_year = request.json['admissionYear']

        if len(school_id) != 10:
            return Response('', 204)

        school = SchoolModel.objects(school_id=school_id).first()
        if not school:
            return Response('', 204)

        if AccountModel.objects(school=school).count() == 0:
            # 해당 학교의 첫 가입자가 관리자
            is_admin = True
            # school_parser.parse_school_schedules(school_id)
        else:
            is_admin = False

        user = AccountModel.objects(id=get_jwt_identity()).first()
        user.update(
            is_admin=is_admin,
            requested=True,
            signed=True if is_admin else False,
            waiting=False if is_admin else True,
            school=school,
            admission_year=admission_year
        )

        return Response('', 201)

    @swag_from(SCHOOL_SIGNUP_GET)
    @auth_required
    def get(self):
        """
        자신의 학교 가입 상태 확인
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()

        return {
            'schoolName': user.school.name if user.school else None,
            'requested': user.requested,
            'signed': None if user.waiting else user.signed
        }
