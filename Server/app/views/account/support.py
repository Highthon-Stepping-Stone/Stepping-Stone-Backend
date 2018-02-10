from flask import Blueprint, Response
from flask_restful import Api, current_app, request
from flasgger import swag_from

from app.docs.account.support import SCHOOL_GET
from app.views import BaseResource, auth_required, json_required

api = Api(Blueprint('account-support-api', __name__))


@api.resource('/school')
class School(BaseResource):
    @swag_from(SCHOOL_GET)
    def get(self):
        """
        학교 검색
        """
