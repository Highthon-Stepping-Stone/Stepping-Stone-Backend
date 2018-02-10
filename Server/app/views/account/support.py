import re

from flask import Blueprint
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.account.support import *
from app.models.school import SchoolModel
from app.views import BaseResource

api = Api(Blueprint('account-support-api', __name__))


@api.resource('/school')
class SchoolSearch(BaseResource):
    @swag_from(SCHOOL_GET)
    def get(self):
        """
        학교 검색
        """
        keyword = request.json['keyword']

        regex = re.compile('.*{}.*'.format(keyword))

        return self.unicode_safe_json_response([{
            'schoolId': school.id,
            'schoolName': school.name
        } for school in SchoolModel.objects(name=regex)])
