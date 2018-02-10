from bson.objectid import ObjectId

from app.models import *


class FolderBase(EmbeddedDocument):
    """
    특정 날짜에 할당해서 사진을 모아 관리하는 '폴더'
    학사일정 앨범에 들어가는 폴더, 자유게시판 앨범에 들어가는 폴더의 schema가 따로 있어서 Base를 만들고 상속 가능하도록 설계
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    id = ObjectIdField(
        primary_key=True,
        default=ObjectId()
    )

    assigned_date = StringField(
        required=True
    )
    # 해당 폴더가 할당된 date

    image_names = ListField(
        StringField(
            required=True
        )
        # default={}
    )


class ScheduledFolderModel(FolderBase):
    pass


class FreeFolderModel(FolderBase):
    pass


class AlbumBase(EmbeddedDocument):
    """
    폴더들을 모아 관리하는 '앨범'
    앨범은 학사일정 앨범과 자유게시판으로 나뉘며, 따로 관리하기 위해 상속 구조 사용
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    id = ObjectIdField(
        primary_key=True,
        default=ObjectId()
    )


class ScheduledAlbumModel(AlbumBase):
    folders = EmbeddedDocumentListField(
        document_type=ScheduledFolderModel
    )


class FreeAlbumModel(AlbumBase):
    folders = EmbeddedDocumentListField(
        document_type=FreeFolderModel
    )


class SchoolModel(Document):
    """
    각 학교를 다루는 모델
    scheduled/free album 을 EmbeddedDocument로 갖는 엄청 큼지막한 컬렉션
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
        # default={}
    )

    scheduled_album = EmbeddedDocumentField(
        document_type=ScheduledAlbumModel
    )

    free_album = EmbeddedDocumentField(
        document_type=FreeAlbumModel
    )
