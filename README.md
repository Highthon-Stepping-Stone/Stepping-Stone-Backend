# Stepping-Stone-Backend [![Build Status](https://travis-ci.org/Highthon-Stepping-Stone/Stepping-Stone-Backend.svg?branch=develop)](https://travis-ci.org/Highthon-Stepping-Stone/Stepping-Stone-Backend) [![Coverage Status](https://coveralls.io/repos/github/Highthon-Stepping-Stone/Stepping-Stone-Backend/badge.svg?branch=develop)](https://coveralls.io/github/Highthon-Stepping-Stone/Stepping-Stone-Backend?branch=develop)

## Technical Stacks
### Dev
#### Software Stack
Python&Flask

#### External Packages
[requirements.txt](./requirements.txt)

#### Database
MongoDB + Redis

#### API Architecture
Serverless

### Ops
#### API Documentation
Swagger

#### Continuous Integration
<a href="https://travis-ci.org/Highthon-Stepping-Stone/Stepping-Stone-Backend">Travis-CI</a>

#### Test Coverage Management
<a href="https://coveralls.io/github/Highthon-Stepping-Stone/Stepping-Stone-Backend?branch=develop">Coveralls</a>

#### Continuous Delivery(Deployment Automation)
Automate zappa deploy&update

#### Container
Docker

#### Log management
JSON format + HDFS + ELK Stack

#### Service Monitoring
New Relic

#### Message Queue
Kafka

#### Another infrastructure
AWS S3, Amazon EC2(for dockerized DB), AWS Lambda, AWS API Gateway, AWS CloudFront(CDN 서비스)

## API Security Checklist
### 인증 (Authentication)
- [x] `Basic Auth`를 사용하지 말고 표준 인증방식을 사용하세요. (예로, JWT, OAuth 등)
- [x] `인증`, `토큰 생성`, `패스워드 저장`은 직접 개발하지 말고 표준을 사용하세요.
- [ ] 로그인에서 `Max Retry`와 격리 기능을 사용하세요.
- [x] 민감한 데이터는 암호화하세요.

#### JWT (JSON Web Token)
- [x] 무작위 대입 공격을 어렵게 하기 위해 랜덤하고 복잡한 키값 (`JWT Secret`)을 사용하세요.
- [x] 요청 페이로드에서 알고리즘을 가져오지 마세요. 알고리즘은 백엔드에서 강제로 적용하세요. (`HS256` 혹은 `RS256`)
- [x] 토큰 만료 기간 (`TTL`, `RTTL`)은 되도록 짧게 설정하세요.
- [x] JWT 페이로드는 [디코딩이 쉽기](https://jwt.io/#debugger-io) 때문에 민감한 데이터는 저장하지 마세요.

### 접근 (Access)
- [ ] DDoS나 무작위 대입 공격을 피하려면 요청 수를 제한하세요. (Throttling)
- [ ] MITM (중간자 공격)을 피하려면 서버 단에서 HTTPS를 사용하세요.
- [ ] SSL Strip 공격을 피하려면 `HSTS` 헤더를 SSL과 함께 사용하세요.

### 입력 및 요청 (Input)
- [x] 각 요청 연산에 맞는 적절한 HTTP 메서드를 사용하세요. `GET (읽기)`, `POST (생성)`, `PUT (대체/갱신)`, `DELETE (삭제)`
- [x] 여러분이 지원하는 포맷 (예를 들어 `application/xml`이나 `application/json` 등)만을 허용하기 위해서는 요청의 Accept 헤더의 `content-type`을 검증하여 매칭되는 게 없을 경우엔 `406 Not Acceptable`로 응답하세요.
- [x] 요청받은 POST 데이터의 `content-type`을 검증하세요. (예를 들어 `application/x-www-form-urlencoded`나 `multipart/form-data` 또는 `application/json` 등)
- [x] 일반적인 취약점들을 피하기 위해선 사용자 입력의 유효성을 검증하세요. (예를 들어 `XSS`, `SQL-Injection` 또는 `Remote Code Execution` 등)
- [x] URL에는 그 어떤 민감한 데이터 (`자격 인증 (crendentials)`, `패스워드`, `보안 토큰` 또는 `API 키`)도 포함하고 있어서는 안 되며 이러한 것들은 표준 인증 방식의 헤더를 사용하세요.
- [ ] 캐싱과 속도 제한 정책을(예를 들어 `Quota`, `Spike Arrest`, `Concurrent Rate Limit`) 제공하는 API 게이트웨이 서비스를 사용하세요. 그리고 API 리소스를 동적으로 배포하세요.

### 서버 처리
- [x] 잘못된 인증을 피하기 위해 모든 엔드포인트가 인증 프로세스 뒤에서 보호되고 있는지 확인하세요.
- [x] 사용자의 리소스 식별자를 사용하는 건 지양하세요. `/user/654321/orders` 대신 `/me/orders`를 사용하세요.
- [x] 자동 증가 (auto-increment) 식별자 대신 `UUID`를 사용하세요.
- [ ] XML 파일을 파싱하고 있다면, `XXE` (XML 외부 엔티티 공격, XML external entity attack)를 피하기 위해 엔티티 파싱을 비활성화하세요.
- [ ] XML 파일을 파싱하고 있다면, 지수적 엔티티 확장 공격을 통한 빌리언 러프/XML 폭탄을 피하기 위해 엔티티 확장을 비활성화하세요.
- [x] 파일 업로드에는 CDN을 사용하세요.
- [x] 거대한 양의 데이터를 다루고 있다면, HTTP 블로킹을 피하고 응답을 빠르게 반환하기 위해 워커나 큐를 사용하세요.
- [x] 디버그 모드를 꺼놓는 일을 절대 잊지 마세요.

### 반환 및 응답 (Output)
- [x] `X-Content-Type-Options: nosniff` 헤더를 반환하세요.
- [x] `X-Frame-Options: deny` 헤더를 반환하세요.
- [ ] `Content-Security-Policy: default-src 'none'` 헤더를 반환하세요.
- [x] `X-Powered-By`, `Server`, `X-AspNet-Version` 등의 디지털 지문 (fingerprinting) 성격의 헤더는 제거하세요.
- [x] 응답에 `content-type`을 강제하세요. 만약 `application/json` 데이터를 반환하고 있다면 응답의 `content-type`은 `application/json`입니다.
- [x] `자격 인증 (crendentials)`, `패스워드`, `보안 토큰`과 같은 민감한 데이터는 반환하지 마세요.
- [x] 각 연산에 맞는 적절한 상태 코드를 반환하세요. (예를 들어 `200 OK`, `400 Bad Request`, `401 Unauthorized`, `405 Method Not Allowed` 등)

### CI & CD
- [x] 단위/통합 테스트 범위로 설계 및 구현을 검토하세요.
- [x] 코드 리뷰 절차를 사용하고 자체 승인을 무시하세요.
- [ ] 제품 출시전에 백신 소프트웨어로 공급 업체의 라이브러리 및 기타 종속적인 것을 포함한 서비스의 모든 구성 요소들을 정적으로 검사했는지 확인하세요.
- [ ] 배포에 대한 롤백 솔루션을 설계하세요.
