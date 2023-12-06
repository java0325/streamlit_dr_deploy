
## 실패


# # streamlit-authenticator는 Streamlit 애플리케이션에 사용자 인증 기능을 추가하는 데 사용할 수 있는 유용한 라이브러리입니다. 
# # 이 라이브러리를 사용하여 간단한 로그인 양식을 구현하는 방법을 단계별로 설명하겠습니다.

# # 설치 
# # 먼저, streamlit-authenticator 라이브러리를 설치해야 합니다. 이는 터미널 또는 명령 프롬프트를 통해 수행할 수 있습니다:
# # pip install streamlit-authenticator
# # 기본 사용 예제
# # 아래는 streamlit-authenticator를 사용하여 기본 로그인 시스템을 구현하는 간단한 예제 코드입니다:

# import streamlit as st
# import streamlit_authenticator as stauth

# # 사용자 이름과 비밀번호 해시를 정의합니다.
# names = ['John Doe', 'Jane Doe']
# usernames = ['johndoe', 'janedoe']
# passwords = ['123', '456']

# # 비밀번호를 해시화합니다.
# hashed_passwords = stauth.Hasher(passwords).generate()

# # 인증 객체를 생성합니다.
# # authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
# #     'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)


# # 기존 코드에서 인자 순서 및 이름을 확인합니다.
# # authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
# #     'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)


# # Assume Authenticate expects the following arguments in order:
# # names, usernames, hashed_passwords, 'cookie_name', 'signature_key', and cookie_expiry_days
# # authenticator = stauth.Authenticate(
# #     names=names, 
# #     usernames=usernames, 
# #     hashed_passwords=hashed_passwords,
# #     cookie_name='some_cookie_name', 
# #     signature_key='some_signature_key', 
# #     cookie_expiry_days=30
# # )


# # Assuming the correct parameters for Authenticate are:
# # usernames, hashed_passwords, cookie_name, signature_key, and cookie_expiry_days
# authenticator = stauth.Authenticate(
#     usernames=usernames, 
#     hashed_passwords=hashed_passwords,
#     cookie_name='some_cookie_name', 
#     signature_key='some_signature_key', 
#     cookie_expiry_days=30
# )



# # 로그인 페이지를 만듭니다.
# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     st.write(f'Welcome *{name}*')
#     # 로그인 후의 코드를 여기에 작성합니다.
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')

import streamlit as st
import streamlit_authenticator as stauth

# 사용자 이름과 비밀번호 해시를 정의합니다.
usernames = ['johndoe', 'janedoe']
passwords = ['123', '456']

# 비밀번호를 해시화합니다.
hashed_passwords = stauth.Hasher(passwords).generate()

# 인증 객체를 생성합니다.
authenticator = stauth.Authenticate(
    'some_cookie_name', 
    'some_signature_key', 
    cookie_expiry_days=30,
    names=usernames, 
    username_passwords=zip(usernames, hashed_passwords)
)

# 로그인 페이지를 만듭니다.
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.write(f'Welcome *{name}*')
    # 로그인 후의 코드를 여기에 작성합니다.
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
