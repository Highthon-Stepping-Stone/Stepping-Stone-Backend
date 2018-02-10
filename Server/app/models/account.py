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

    is_admin = BooleanField(
        required=True,
        default=False
    )
    accepted = BooleanField(
        required=True,
        default=False
    )

    school = ReferenceField(
        document_type=SchoolModel,
        required=True
    )
    admission_year = IntField(
        required=True
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
        document_type=AccountModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    pw_snapshot = StringField(
        required=True
    )
