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
        },
        {
            'name': 'schoolId',
            'description': '학교 검색 시 함께 리턴되었던 학교 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'admissionYear',
            'description': '입학년도',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공, 추가 정보를 입력하는 API를 이용해 나머지 정보를 올려 주어야 함.',
        },
        '204': {
            'description': 'ID 중복으로 인해 회원가입 실패'
        },
        '205': {
            'description': '존재하지 않는 school id'
        }
    }
}
