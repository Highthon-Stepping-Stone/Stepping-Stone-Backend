import unittest as ut

from app.models.school import SchoolModel

from server import app
from utils import school_parser


if __name__ == '__main__':
    app.testing = True

    SchoolModel(school_id='G100000170', web_url='stu.dje.go.kr', name='대덕소프트웨어마이스터고등학교').save()
    school_parser.parse_school_schedules('1234')
    # TODO 나이스 문제 없어지면 하드코딩 제거해야 함

    all_tests = ut.TestLoader().discover('tests', '*.py')
    ut.TextTestRunner().run(all_tests)
