from flask import Blueprint, Response
from flask_restful import Api, request
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.docs.account.signup import *
from app.models.account import AccountModel
from app.models.school import SchoolModel
from app.views import BaseResource, json_required

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
        school_id = request.json['schoolId']
        admission_year = request.json['admissionYear']

        hashed_pw = generate_password_hash(pw)

        if AccountModel.objects(id=id).first():
            return Response('', 204)

        if len(school_id) != 24:
            return Response('', 205)

        school = SchoolModel.objects(school_id=school_id).first()
        if not school:
            return Response('', 205)

        if AccountModel.objects(id=id, school=school).count() == 0:
            # 해당 학교의 첫 가입자가 관리자
            is_admin = accepted = True
        else:
            is_admin = accepted = False

        AccountModel(
            id=id,
            pw=hashed_pw,
            is_admin=is_admin,
            accepted=accepted,
            admission_year=admission_year
        ).save()

        return Response('', 201)
