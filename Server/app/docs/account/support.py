SCHOOL_POST = {
    'tags': ['계정'],
    'description': '학교 검색',
    'parameters': [
        {
            'name': 'keyword',
            'description': '검색 시 사용할 keyword',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '검색 완료. 학교 정보들이 반환되며, 검색 결과가 없는 경우 length가 0입니다.',
            'examples': {
                '': [
                    {
                        'schoolId': '0eb129d8c528d872a153c',
                        'schoolName': '대덕소프트웨어마이스터고등학교'
                    },
                    {
                        'schoolId': '0eb129d8c528d872a153d',
                        'schoolName': '선린인터넷고등학교'
                    }
                ]
            }
        }
    }
}

INFO_GET = {
    'tags': ['계정'],
    'description': '자신과 소속 학교 관련 정보 획득',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                '': {
                    'isAdmin': True,
                    'members': [
                        {
                            'id': 'planb',
                            'name': '윤여횐',
                            'admissionYear': 2000,
                            'isAdmin': False
                        },
                        {
                            'id': 'planb2',
                            'name': '정경서',
                            'admissionYear': 2010,
                            'isAdmin': False
                        }
                    ]
                }
            }
        },
        '403': {
            'description': '권한 없거나 소속 학교 없음'
        }
    }
}
