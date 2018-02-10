from functools import wraps
import ujson
import time

from flask import Response
from flask_restful import Resource, abort, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.account import AccountBase


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        user = AccountBase.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        return fn(*args, **kwargs)

    return wrapper


def json_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            abort(406)

        return fn(*args, **kwargs)

    return wrapper


class BaseResource(Resource):
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_response(cls, data, status_code=200):
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views.account import auth, signup, support
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(support.api.blueprint)
