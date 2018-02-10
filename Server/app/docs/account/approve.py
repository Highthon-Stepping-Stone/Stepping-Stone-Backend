APPROVE_SIGNUP_LIST_POST = {
    'tags': ['가입 승인'],
    'description': '가입 승인 요청자 목록 조회',
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
            'description': '가입 승인 요청자 조회 성공',
            'examples': {
                '': [
                    {
                        'id': 'planb',
                        'name': '김형규',
                        'admissionYear': 2017
                    },
                    {
                        'id': 'planb2',
                        'name': '김규형',
                        'admissionYear': 2016
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

APPROVE_SIGNUP_POST = {
    'tags': ['가입 승인'],
    'description': '가입 요청 승인',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '가입을 승인할 사용자의 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '가입 승인 성공'
        },
        '204': {
            'description': '해당 ID를 가진 사용자 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

APPROVE_SIGNUP_DELETE = {
    'tags': ['가입 승인'],
    'description': '가입 요청 거절',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '가입을 거절할 사용자의 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '가입 거절 성공'
        },
        '204': {
            'description': '해당 ID를 가진 사용자 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
