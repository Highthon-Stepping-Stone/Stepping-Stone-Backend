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
            'name': 'name',
            'description': '사용자 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공',
        },
        '204': {
            'description': 'ID 중복으로 인해 회원가입 실패'
        }
    }
}

SCHOOL_SIGNUP_POST = {
    'tags': ['가입 요청'],
    'description': '학교에 가입 요청',
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
            'name': 'admissionYear',
            'description': '입학년도',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '가입 요청 성공',
        },
        '204': {
            'description': '존재하지 않는 school id'
        }
    }
}

SCHOOL_SIGNUP_GET = {
    'tags': ['가입 요청'],
    'description': '자신의 가입 요청 상태 확인',
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
            'description': """
            가입 요청 상태 확인 성공. requested는 자신이 가입 요청을 보냈는지(true: 보냄, false: 보내지 않음)를 의미하며
            signed는 자신의 학교 가입 상태를 의미합니다.(true: 가입됨, false: 가입되지 않음)
            - 가능한 조합은
            requested: true, signed: true = 가입 요청을 보냈으며, 승인받아 가입된 상태
            requested: true, signed: false = 가입 요청을 보냈으나 관리자가 거절한 상태
            requested: true, signed: null = 가입 요청을 보냈으며, 관리자가 아직 처리하지 않은 상태
            requested: false, signed: false = 가입 요청을 보내지 않았고, 가입되지 않은 상태
            requested: false, signed: true = 해당 경우 없음
            """,
            'examples': {
                '': {
                    'schoolName': '대덕소프트웨어마이스터고등학교',
                    'requested': True,
                    'signed': None
                }
            }
        }
    }
}
