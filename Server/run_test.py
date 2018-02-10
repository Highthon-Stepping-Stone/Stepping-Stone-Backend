import unittest as ut

from server import app
from utils import school_parser

if __name__ == '__main__':
    app.testing = True

    school_parser.parse_school_list_from_excel()

    all_tests = ut.TestLoader().discover('tests', '*.py')
    ut.TextTestRunner().run(all_tests)
