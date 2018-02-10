SIGNUP_POST = {
    'tags': ['계정'],
    'description': '서비스 자체 회원가입. 학교/학년, 반 등 추가 데이터는 SNS 연동 기능과의 일관성을 위해 API가 분리되어 있습니다.',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '사용자 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공, 추가 정보를 입력하는 API를 이용해 나머지 정보를 올려 주어야 함.',
        },
        '204': {
            'description': 'ID 중복으로 인해 회원가입 실패'
        }
    }
}

ADDITIONAL_INFO_POST = {
    'tags': ['계정'],
    'description': 'SNS 계정 최초 로그인, 혹은 서비스 자체 회원가입 시 사용자 추가 정보 입력. 해당 정보가 따로 업로드되지 않을 시 기본값으로 처리되고, 이미 정보가 있는 경우 덮어씌워 집니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'schoolId',
            'description': '학교 검색 시 함께 리턴되었던 학교 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'grade',
            'description': '사용자의 학년',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'class',
            'description': '사용자의 반',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '업로드 성공'
        },
        '204': {
            'description': '존재하지 않는 school id'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
