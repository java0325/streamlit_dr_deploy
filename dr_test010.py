# keypoints 구현완료
# body_speed, stride, cardence(steps) 구현완료

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# CSV 파일 경로 설정
file_path = 'dr_rec003.csv'
# CSV 파일을 'cp949' 또는 'euc-kr' 인코딩으로 읽기
df = pd.read_csv(file_path, encoding='cp949')  # 또는 encoding='euc-kr'

# Streamlit 애플리케이션 시작
st.title('Video analysis results')

# Sidebar에 날짜 선택 옵션 추가
selected_date = st.sidebar.selectbox('Please choose a training date👏', df['date'])

# 선택한 날짜에 해당하는 데이터 추출
selected_data = df[df['date'] == selected_date]

# 선택한 날짜에 대한 데이터 표시
st.write(f"### Analysis results: {selected_date}")
st.table(selected_data[['place', 'company', 'runner_name']])

# # 비디오 파일 경로 가져오기
# video_file = selected_data['video_file'].values[0]

# # 이미지 로딩 및 데이터 값 표시를 같은 행에 배치
# col1, col2 = st.columns(2)  # 2개의 컬럼 생성

# # 첫 번째 컬럼에 이미지 표시
# with col1:
#     video_bytes = open(video_file, 'rb').read()
#     st.video(video_bytes)

# 이미지 파일 경로 가져오기
img_file = selected_data['img_file'].values[0]

# 이미지 로딩 및 데이터 값 표시를 같은 행에 배치
col1, col2 = st.columns(2)  # 2개의 컬럼 생성

# 첫 번째 컬럼에 이미지 표시
with col1:
    image = Image.open(img_file)
    st.image(image, use_column_width=True)

# CSV 파일 로드
csv_file = selected_data['body_speed_csv_file'].values[0]
df_body_speed = pd.read_csv(csv_file)

# # body_speed의 평균값 계산
# average_speed = df_body_speed['body_speed'].mean()

# body_speed의 평균값을 소수점 둘째자리까지 계산
average_speed = round(df_body_speed['body_speed'].mean(), 2)

# CSV 파일 로드
csv_file2 = selected_data['stride_cadence_csv_file'].values[0]
df_stride_cadence = pd.read_csv(csv_file2)

# Stride와 Cadence의 평균값 계산 (소수점 둘째자리까지)
average_stride = round(df_stride_cadence['stride'].mean(), 2)
average_cadence = round(df_stride_cadence['cadence'].mean(), 2)

# 두 번째 컬럼에 데이터 값 표시
with col2:
    st.write(f'Average Speed: {average_speed} m/s')    
    st.write(f'Stride: {average_stride} m')  # 수정된 부분
    st.write(f'Cadence: {average_cadence} steps/m')  # 수정된 부분     

# CSV 파일 로드
csv_file = selected_data['body_speed_csv_file'].values[0]
df_body_speed = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Body Speed Data Trends')

# 데이터프레임 그룹화
grouped = df_body_speed.groupby('video_id')

# 각 그룹에 대한 그래프 그리기
for video_id, group_data in grouped:
    fig, ax = plt.subplots(figsize=(8, 4))  # 1행 1열의 서브플롯 생성

    # body_speed 데이터 그래프
    ax.plot(group_data['index'], group_data['body_speed'], label='body_speed')  # body_speed 그래프 추가
    ax.set_title(f'Body Speed for Video ID {video_id}')  # 그래프 제목 수정

    # 그래프 스타일 및 레이블 설정
    ax.set_xlabel('Index')
    ax.set_ylabel('Body Speed')
    ax.legend()  # 범례 표시

    # 서브플롯 레이아웃 조정
    plt.tight_layout()

    # 그래프를 Streamlit 애플리케이션에 표시
    st.pyplot(fig)

# CSV 파일 로드
csv_file = selected_data['stride_cadence_csv_file'].values[0]
df_stride_cadence = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Stride and Cadence Data Trends')

# 데이터프레임 그룹화
grouped = df_stride_cadence.groupby('video_id')

# 각 그룹에 대한 그래프 그리기
for video_id, group_data in grouped:
    # stride 데이터 그래프 생성 및 표시
    fig_stride, ax_stride = plt.subplots(figsize=(8, 4))
    ax_stride.plot(group_data['stride_index'], group_data['stride'], label='stride')
    ax_stride.set_title(f'Stride for Video ID {video_id}')
    ax_stride.set_xlabel('Index')
    ax_stride.set_ylabel('Stride')
    ax_stride.legend()
    plt.tight_layout()
    st.pyplot(fig_stride)
    plt.close(fig_stride)

    # cadence 데이터 그래프 생성 및 표시
    fig_cadence, ax_cadence = plt.subplots(figsize=(8, 4))
    ax_cadence.plot(group_data['stride_index'], group_data['cadence'], label='cadence')
    ax_cadence.set_title(f'Cadence for Video ID {video_id}')
    ax_cadence.set_xlabel('Index')
    ax_cadence.set_ylabel('Cadence')
    ax_cadence.legend()
    plt.tight_layout()
    st.pyplot(fig_cadence)
    plt.close(fig_cadence)

# import pandas as pd
# import matplotlib.pyplot as plt
# import streamlit as st

# CSV 파일 로드
csv_file = selected_data['keypoints_csv_file'].values[0]
df_keypoints = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Keypoints Data Trends')

# 데이터프레임 그룹화
grouped = df_keypoints.groupby('video_id')

# 그래프를 그릴 컬럼 목록 (video_id 제외)
columns_to_plot = [
    'angles_left_leg_up', 'angles_right_leg_up', 'angles_core_decline',
    'angles_left_knee', 'angles_right_knee', 'knee_left_leftright',
    'knee_left_updown', 'knee_right_leftright', 'knee_right_updown',
    'ankle_left_leftright', 'ankle_left_updown', 'ankle_right_leftright',
    'ankle_right_updown', 'hip_left_leftright', 'hip_left_updown',
    'hip_right_leftright', 'hip_right_updown', 'wrist_left_leftright',
    'wrist_left_updown', 'wrist_right_leftright', 'wrist_right_updown'
]

# 각 그룹에 대한 그래프 그리기
for video_id, group_data in grouped:
    # 컬럼별로 그래프 생성 및 표시
    for column in columns_to_plot:
        fig, ax = plt.subplots(figsize=(8, 4))
        
        ax.plot(group_data[column], label=column)  # 해당 컬럼의 그래프 추가
        ax.set_title(f'{column} for Video ID {video_id}')
        ax.set_xlabel('Index')
        ax.set_ylabel(column)
        ax.legend()
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
