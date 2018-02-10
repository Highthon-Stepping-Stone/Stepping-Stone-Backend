import re

from flask import Blueprint, abort
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.account.support import *
from app.models.account import AccountModel
from app.models.school import SchoolModel
from app.views import BaseResource, auth_required

api = Api(Blueprint('account-support-api', __name__))


@api.resource('/school')
class SchoolSearch(BaseResource):
    @swag_from(SCHOOL_POST)
    def post(self):
        """
        학교 검색
        """
        keyword = request.json['keyword']

        regex = re.compile('.*{}.*'.format(keyword))

        return self.unicode_safe_json_response([{
            'schoolId': school.id,
            'schoolName': school.name
        } for school in SchoolModel.objects(name=regex)])


@api.resource('/info')
class Info(BaseResource):
    @swag_from(INFO_GET)
    @auth_required
    def get(self):
        """
        계정 정보 획득
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()

        if not user.school:
            abort(403)

        response = {
            'isAdmin': user.is_admin,
            'members': [{
                'id': member.id,
                'name': member.name,
                'admissionYear': member.admission_year,
                'isAdmin': member.is_admin
            } for member in AccountModel.objects if member.id != user.id]
        }

        return self.unicode_safe_json_response(response)
