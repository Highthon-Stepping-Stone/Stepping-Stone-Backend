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
