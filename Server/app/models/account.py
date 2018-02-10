from datetime import datetime

from app.models import *
from app.models.school import SchoolModel


class AccountModel(Document):
    meta = {
        'collection': 'account'
    }

    signup_time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    id = StringField(
        primary_key=True
    )
    pw = StringField(
        required=True
    )
    name = StringField(
        required=True
    )

    is_admin = BooleanField()

    requested = BooleanField(
        required=True,
        default=False
    )
    # 가입 요청을 이미 보냈는지의 여부
    signed = BooleanField(
        required=True,
        default=False
    )

    school = ReferenceField(
        document_type=SchoolModel
    )
    admission_year = IntField()


class RefreshTokenModel(Document):
    """
    Manages JWT refresh token
    """
    meta = {
        'collection': 'refresh_token'
    }

    token = UUIDField(
        primary_key=True
    )
    token_owner = ReferenceField(
        document_type=AccountModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    pw_snapshot = StringField(
        required=True
    )
