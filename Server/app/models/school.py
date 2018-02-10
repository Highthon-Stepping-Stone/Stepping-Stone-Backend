from app.models import *


class SchoolModel(Document):
    meta = {
        'collection': 'school'
    }

    name = StringField(
        required=True
    )
