<h1>장고 심화 개인 과제</h1>
<h2>Todo List를 DRF로 만들어보기</h2><br>

<h3>구현 기능</h3>
<p>USER</p>
<li>회원가입(POST) : 필수 필드(id, email, password, name, gender, age, introduntion)</li>
<li>로그인(POST)</li>
<li>로그아웃(POST) : 미구현</li>
<li>회원 정보 수정(PUT)</li>
<li>회원 탈퇴(DELETE)</li><br>

<p>TODO</p>
<li>할일 만들기(POST) : 필수 필드(id, title, is_complete, created_at, updated_at, 
                    completion_at, user_id(FK))</li>
<li>할일 목록 조회(GET)</li>
<li>할일 수정(PUT)</li>
<li>할일 삭제(DELETE)</li><br>

<p>추가</p>
<li>작성자 본인만 조회, 수정, 삭제 가능</li>
<li>JWT 방식 : accesss 토큰 payload 정보(user email, name, gender, age)</li><br>


<h3>ERDcloud</h3>

![image](https://user-images.githubusercontent.com/127708804/234277705-e898a5b4-9722-4196-9a1c-2d953ce21392.png)
