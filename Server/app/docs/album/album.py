SCHEDULED_ALBUM_POST = {
    'tags': ['앨범'],
    'description': '학사일정 앨범에 사진 추가',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'date',
            'description': '사진을 추가할 날짜',
            'in': 'query',
            'type': 'str',
            'required': True
        },
        {
            'name': 'file',
            'description': '어떤 key로든 0개 이상의 파일을 multipart/form-data로 업로드합니다.',
            'in': 'formData',
            'type': 'file',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '업로드 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SCHEDULED_ALBUM_GET = {
    'tags': ['앨범'],
    'description': '학사일정 앨범 데이터 불러오기',
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
            'description': '데이터 불러오기 성공.',
            'examples': {
                '': [
                    {
                        '2018-01-01': {
                            'scheduleNames': ['새해', '마이스터고 협의회'],
                            'folder': {
                                # 'folderId': '0eb129d8c528d872a153c',
                                'imageNames': [
                                    '2903bff771534e00b64fb1e053684994.png',
                                    'da9f07cb5ba541d8a3a3ed97838d8c43.png',
                                    'c05307c463924c5fb8db74314650036a.png'
                                ],
                                'imageCount': 3
                            }
                        }
                    },
                    {
                        '2018-02-05': {
                            'scheduleNames': ['개학식', '듣기평가'],
                            'folder': {
                                # 'folderId': '0eb129d8c528d872a153c',
                                'imageNames': [],
                                'imageCount': 0
                            }
                        }
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
