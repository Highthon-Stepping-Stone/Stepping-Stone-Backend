from datetime import datetime

from app.models import *


class AccountBase(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    signup_time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    id = StringField(
        primary_key=True
    )

    school_name = StringField(
        required=True,
        default='학교 없음'
    )
    grade = IntField(
        required=True,
        default=1
    )
    class_ = IntField(
        required=True,
        default=1
    )


class ServiceAccountModel(AccountBase):
    meta = {
        'collection': 'service_account'
    }

    pw = StringField(
        required=True
    )


class SNSAccountModel(AccountBase):
    meta = {
        'collection': 'sns_account'
    }

    connected_service = StringField(
        required=True,
        default='Facebook'
    )


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
        document_type=AccountBase,
        required=True,
        reverse_delete_rule=CASCADE
    )
    pw_snapshot = StringField(
        required=True
    )
