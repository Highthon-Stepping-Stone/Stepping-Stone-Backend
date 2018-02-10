AUTH_POST = {
    'tags': ['계정'],
    'description': '서비스 자체 계정 로그인',
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
        '200': {
            'description': '로그인 성공. Access Token과 Refresh Token을 반환합니다.',
            'examples': {
                '': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M',
                    'refreshToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM5MDQ3NjMsImlkZW50aXR5IjoibmlsIiwiZnJlc2giOmZhbHNlLCJqdGkiOiI1Yzg1ZDAxNy1lYjIwLTRmYjgtYmVhYi1iYmYyZTQyY2NlYmYiLCJuYmYiOjE1MTM2NDU1NjMsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE1MTM2NDU1NjN9.075C0_-b-oqSWc-jz7G35y00erRVntpcqN9uMIAnvfI'
                }
            }
        }
    }
}

SNS_AUTH_POST = {
    'tags': ['계정'],
    'description': 'SNS 계정으로 로그인',
    'parameters': [
        {
            'name': 'id',
            'description': 'SNS 계정 ID(SNS 계정 연동 API마다 존재하는, 사용자마다 할당되며 mutable한 아주 긴 ID)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'connected_service',
            'description': '연결된 서비스(Facebook or Google)',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공(이미 가입되어 있는 계정)',
            'examples': {
                '': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M',
                    'refreshToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM5MDQ3NjMsImlkZW50aXR5IjoibmlsIiwiZnJlc2giOmZhbHNlLCJqdGkiOiI1Yzg1ZDAxNy1lYjIwLTRmYjgtYmVhYi1iYmYyZTQyY2NlYmYiLCJuYmYiOjE1MTM2NDU1NjMsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE1MTM2NDU1NjN9.075C0_-b-oqSWc-jz7G35y00erRVntpcqN9uMIAnvfI'
                }
            }
        },
        '201': {
            'description': '로그인 성공(서비스에 최초로 로그인해 자동으로 회원가입 처리됨), 추가 정보를 입력하는 API를 이용해 나머지 정보를 올려 주어야 합니다.'
        }
    }
}

REFRESH_GET = {
    'tags': ['계정'],
    'description': 'JWT Token refresh. 새로운 access token을 얻습니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Refresh Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Refresh 성공. 새로운 access token을 반환합니다.',
            'examples': {
                '': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M',
                }
            }
        },
        '205': {
            'description': '해당 refresh token 발급 시 사용한 비밀번호가 변경되어 재로그인 필요'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
