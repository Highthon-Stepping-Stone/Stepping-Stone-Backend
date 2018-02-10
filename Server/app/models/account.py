from datetime import datetime

from app.models import *
from app.models.school import SchoolModel


class AccountModel(Document):
    """
    사용자 계정을 다루는 모델
    """
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

    is_admin = BooleanField(
        required=True,
        default=False
    )
    # 사용자의 관리자 여부

    requested = BooleanField(
        required=True,
        default=False
    )
    # 가입 요청을 이미 보냈는지의 여부

    signed = BooleanField(
        required=True,
        default=False
    )
    # 학교 가입 상태

    school = ReferenceField(
        document_type=SchoolModel
    )
    # 가입 요청을 보냈거나, 가입되어 있는 학교

    admission_year = IntField()
    # 입학 연도


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
