from app.models import *


class SchoolModel(Document):
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
        # default={}
    )


class AlbumBase(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    school = ReferenceField(
        document_type=SchoolModel,
        required=True
    )


class ScheduledAlbumModel(AlbumBase):
    meta = {
        'collection': 'school_calendar_album'
    }


class FreeAlbumModel(AlbumBase):
    meta = {
        'collection': 'free_album'
    }


class FolderModel(Document):
    meta = {
        'collection': 'folder'
    }

    album = ReferenceField(
        document_type=AlbumBase,
        required=True
    )

    image_names = ListField(
        StringField(
            required=True
        )
        # default={}
    )
