# 로그인 샘플 구현

import streamlit as st
from streamlit_authenticator import Authenticate

# 사용자 정보 설정
names = ["사용자1", "사용자2"]
usernames = ["user1", "user2"]
passwords = ["password1", "password2"]

# Authenticator 객체 생성
authenticator = Authenticate(names, usernames, passwords, 
                             "some_cookie_name", "some_signature_key", 
                             cookie_expiry_days=30)

# 로그인 폼 생성
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.write(f'안녕하세요 {name}님!')
    # 로그인 후 보여줄 내용
elif authentication_status == False:
    st.error("사용자 이름/비밀번호가 잘못되었습니다.")
elif authentication_status == None:
    st.warning("사용자 이름과 비밀번호를 입력해주세요.")
