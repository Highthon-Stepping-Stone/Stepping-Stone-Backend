from app.models import *
from app.models.school import SchoolModel


class AlbumBase(Document):
    """
    폴더들을 모아 관리하는 '앨범'
    앨범은 학사일정 앨범과 자유게시판으로 나뉘며, 따로 관리하기 위해 상속 구조 사용
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    school = ReferenceField(
        document_type=SchoolModel,
        required=True,
        reverse_delete_rule=CASCADE
    )


class ScheduledAlbumModel(AlbumBase):
    meta = {
        'collection': 'scheduled_album'
    }


class FreeAlbumModel(AlbumBase):
    meta = {
        'collection': 'free_album'
    }


class FolderBase(Document):
    """
    특정 날짜에 할당해서 사진을 모아 관리하는 '폴더'
    학사일정 앨범에 들어가는 폴더, 자유게시판 앨범에 들어가는 폴더의 schema가 따로 있어서 Base를 만들고 상속 가능하도록 설계
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    image_names = ListField(
        StringField(
            required=True
        )
        # default=[]
    )


class ScheduledFolderModel(FolderBase):
    meta = {
        'collection': 'scheduled_folder'
    }

    album = ReferenceField(
        document_type=ScheduledAlbumModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    assigned_date = StringField(
        required=True
    )
    # 해당 폴더가 할당된 date
    # 학사일정 앨범은 날짜 기반으로 폴더를 묶음


class FreeFolderModel(FolderBase):
    meta = {
        'collection': 'free_folder'
    }

    album = ReferenceField(
        document_type=FreeAlbumModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    category_name = StringField(
        required=True,
        default=''
    )

    folder_name = StringField(
        required=True,
        default=''
    )
    # 자유게시판은 카테고리 단위로 폴더를 묶음
