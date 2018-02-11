from uuid import uuid4

from flask import Blueprint, Response, abort, request
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api
from flasgger import swag_from

from app.docs.album.album import *
from app.models.account import AccountModel
from app.models.album import ScheduledAlbumModel, ScheduledFolderModel
from app.models.school import SchoolModel
from app.views import BaseResource, auth_required

api = Api(Blueprint('album-api', __name__))


@api.resource('/album/scheduled')
class ScheduledAlbum(BaseResource):
    @swag_from(SCHEDULED_ALBUM_POST)
    # @auth_required
    def post(self):
        """
        학사일정 앨범에 사진 추가
        """
        date = request.args['date']

        # user = AccountModel.objects(id=get_jwt_identity()).first()
        # if not user:
        #     abort(403)

        # school = user.school
        school = SchoolModel.objects(school_id='G100000170').first()
        album = ScheduledAlbumModel.objects(school=school).first()
        target_folder = ScheduledFolderModel.objects(album=album).first()
        if not target_folder:
            target_folder = ScheduledFolderModel(
                album=album,
                assigned_date=date
            ).save()

        images = request.files.getlist("file[]")

        for image in images:
            extend = image.filename.split('.')[-1]
            # Take extend from image's origin filename

            image_name = uuid4().hex
            image_full_name = '{}.{}'.format(image_name, extend)
            print(image_full_name)

            target_folder.image_names.append(image_full_name)
            print(target_folder.image_names)
            image.save('./static/{}'.format(image_full_name))

        target_folder.save()

        return Response('', 201)

    @swag_from(SCHEDULED_ALBUM_GET)
    @auth_required
    def get(self):
        """
        학사일정 앨범 데이터 조회
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        school = user.school
        album = ScheduledAlbumModel.objects(school=school).first()
        folders = ScheduledFolderModel.objects(album=album)

        response = [{'date': date, 'resource': {'scheduleNames': schedules, 'folder': {}}} for date, schedules in school.schedules.items()]

        for folder in folders:
            if folder.assigned_date not in response:
                # TODO 기타로 넘겨야 함
                continue

            response[folder.assigned_date]['folder'].update({
                # 'folderId': folder.id,
                'imageNames': [image_name for image_name in folder.image_names],
                'imageCount': len(folder.image_names)
            })

        return self.unicode_safe_json_response(response)
