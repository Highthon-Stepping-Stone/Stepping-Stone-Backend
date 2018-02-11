from argparse import ArgumentParser
import os

from app.models.album import FreeAlbumModel, ScheduledAlbumModel
from app.models.school import SchoolModel
from app import app

from utils import school_parser

if __name__ == '__main__':
    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable.')

    parser = ArgumentParser('해당 Flask 어플리케이션이 동작하기 위해 필요한 설정 값들을 다루기 위한 Argument Parser입니다.')

    parser.add_argument('-p', '--port')
    args = parser.parse_args()

    school = SchoolModel(school_id='G100000170', web_url='stu.dje.go.kr', name='대덕소프트웨어마이스터고등학교').save()
    ScheduledAlbumModel(school=school).save()
    FreeAlbumModel(school=school).save()

    school_parser.parse_school_schedules('1234')
    # TODO 나이스 문제 없어지면 하드코딩 제거해야 함

    app.run(host=app.config['HOST'], port=int(args.port) if args.port else app.config['PORT'], debug=app.debug, threaded=True)
