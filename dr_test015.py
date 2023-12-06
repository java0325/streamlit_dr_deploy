# 로그인 처리 수행됨
# 로그인 처리는 성공, 그러나, 뿌려지는 데이터의 수정이 필요하여 미완성 016으로 버전을 옮겨서 수정할 것!!

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Streamlit 애플리케이션의 페이지 설정
st.set_page_config(layout="wide")

# 하드코딩된 사용자 이름과 비밀번호 (실제 사용 시 보안을 강화해야 함)
expected_username = "user1"
expected_password = "password123"

# 로그인 섹션
with st.sidebar:
    st.title("로그인")
    username = st.text_input("사용자 이름")
    password = st.text_input("비밀번호", type="password")
    login_button = st.button("로그인")

# 사용자 인증 확인
if login_button and username == expected_username and password == expected_password:
    # CSV 파일 경로 설정
    file_path = 'dr_rec003.csv'
    df = pd.read_csv(file_path, encoding='cp949')  # 또는 encoding='euc-kr'

    st.title('Video analysis results')

    # Sidebar에 날짜 선택 옵션 추가
    selected_date = st.sidebar.selectbox('Please choose a training date👏', df['date'])

    # 선택한 날짜에 해당하는 데이터 추출
    selected_data = df[df['date'] == selected_date]

    # 데이터프레임을 HTML로 변환
    html = selected_data[['place', 'company', 'runner_name']].to_html(index=False)

    # HTML과 함께 CSS를 사용하여 스타일링 적용
    st.markdown(f"""
    <style>
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    th {{
        color: black;
        background-color: #ADD8E6;
    }}
    td, th {{
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
        font-size: 16px;
        font-weight: bold;
    }}
    </style>
    {html}
    """, unsafe_allow_html=True)

    # 비디오 파일 경로 설정 및 표시
    filename = "output_20230902_002_h264_codec.mp4"
    video_file = open(filename, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    # CSV 파일 로드 및 body_speed의 평균값 계산
    csv_file = selected_data['body_speed_csv_file'].values[0]
    df_body_speed = pd.read_csv(csv_file)
    average_speed = round(df_body_speed['body_speed'].mean(), 2)

    # 두 번째 CSV 파일 로드 및 Stride와 Cadence의 평균값 계산
    csv_file2 = selected_data['stride_cadence_csv_file'].values[0]
    df_stride_cadence = pd.read_csv(csv_file2)
    average_stride = round(df_stride_cadence['stride'].mean(), 2)
    average_cadence = round(df_stride_cadence['cadence'].mean(), 2)

    # 데이터 값 표시 (이미지 아래)
    st.markdown(f'<h3 style="color:blue;">✔ <b>Average Speed:</b> {average_speed} m/s</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color:blue;">✔ <b>Stride:</b> {average_stride} m</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color:blue;">✔ <b>Cadence:</b> {average_cadence} steps/m</h3>', unsafe_allow_html=True)

    # Body Speed Data Trends 그래프 표시
    csv_file = selected_data['body_speed_csv_file'].values[0]
    df_body_speed = pd.read_csv(csv_file)
    st.write('## Body Speed Data Trends')
    grouped = df_body_speed.groupby('video_id')
    for video_id, group_data in grouped:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(group_data['index'], group_data['body_speed'], label='body_speed')
        ax.set_title(f'Body Speed for Video ID {video_id}')
        ax.set_xlabel('Index')
        ax.set_ylabel('Body Speed')
