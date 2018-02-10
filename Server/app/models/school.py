from app.models import *


class SchoolModel(Document):
    """
    각 학교를 다루는 모델
    """
    meta = {
        'collection': 'school'
    }

    school_id = StringField(
        primary_key=True
    )

    web_url = StringField(
        required=True
    )

    name = StringField(
        required=True
    )

    schedules = DictField(
        # {'YYYY-MM-DD': ['', '', ''], ...}
    )
