# video 처리완료

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Streamlit 애플리케이션의 페이지 설정
st.set_page_config(layout="wide")

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

# # # 비디오 파일 경로 설정
# video_file = '/Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/result_6angles230817_2_h264_codec.mp4'

# # 코덱 H264인코딩 문제! 지우지 말것!!
# # ffmpeg -i result_6angles230817_2.mp4 -vcodec libx264 result_6angles230817_2_h264_codec.mp4
# # ffmpeg -i output_kor20230728f00001_20230902_001.mp4 -vcodec libx264 output_kor20230728f00001_20230902_001_h264_codec.mp4

## 비디오파일 자르기
# # ffmpeg -i output_kor20230728f00001_20230902_001_h264_codec.mp4 -ss 00:00:00 -t 00:50:00 output_20230902_001_h264_codec.mp4

## 해상도 조정하기
## ffmpeg -i output_kor20230728f00001_20230902_001_h264_codec.mp4 -vf scale=1280:720 output_20230902_002_h264_codec.mp4
# # # Streamlit을 사용하여 비디오 디스플레이
# # st.video(video_file)

# # 비디오 HTML 태그를 사용하여 비디오 삽입
# video_html = f"""
# <video width="100%" controls>
#   <source src="{video_file}" type="video/mp4">
#   Your browser does not support the video tag.
# </video>
# """
# st.markdown(video_html, unsafe_allow_html=True)

# 비디오 파일 경로 설정
# filename = "/Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/result_6angles230817_2_h264_codec.mp4"
# /Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/output_kor20230728f00001_20230902_001_h264_codec.mp4
# filename = "result_6angles230817_2_h264_codec.mp4"
filename = "output_20230902_002_h264_codec.mp4" 

video_file = open(filename, 'rb')
video_bytes = video_file.read()
st.video(video_bytes) 

# # 이미지 파일 경로 가져오기
# img_file = selected_data['img_file'].values[0]

# # 이미지 로딩
# image = Image.open(img_file)
# st.image(image, use_column_width=True)

# CSV 파일 로드 및 body_speed의 평균값 계산
csv_file = selected_data['body_speed_csv_file'].values[0]
df_body_speed = pd.read_csv(csv_file)
average_speed = round(df_body_speed['body_speed'].mean(), 2)

# 두 번째 CSV 파일 로드 및 Stride와 Cadence의 평균값 계산
csv_file2 = selected_data['stride_cadence_csv_file'].values[0]
df_stride_cadence = pd.read_csv(csv_file2)
average_stride = round(df_stride_cadence['stride'].mean(), 2)
average_cadence = round(df_stride_cadence['cadence'].mean(), 2)

# # 데이터 값 표시 (이미지 아래) - 특수 문자 사용

st.markdown(f'<h3 style="color:blue;">✔ <b>Average Speed:</b> {average_speed} m/s</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="color:blue;">✔ <b>Stride:</b> {average_stride} m</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="color:blue;">✔ <b>Cadence:</b> {average_cadence} steps/m</h3>', unsafe_allow_html=True)


# CSV 파일 로드
csv_file = selected_data['body_speed_csv_file'].values[0]
df_body_speed = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Body Speed Data Trends')

# 데이터프레임 그룹화
grouped = df_body_speed.groupby('video_id')

for video_id, group_data in grouped:
    fig, ax = plt.subplots(figsize=(8, 4))  # 1행 1열의 서브플롯 생성

    # body_speed 데이터 그래프
    ax.plot(group_data['index'], group_data['body_speed'], label='body_speed')  # body_speed 그래프 추가
    ax.set_title(f'Body Speed for Video ID {video_id}')  # 그래프 제목 수정

    # 그래프 스타일 및 레이블 설정
    ax.set_xlabel('Index')
    ax.set_ylabel('Body Speed')
    ax.legend()  # 범례 표시

    # 평균값 표시
    mean_speed = group_data['body_speed'].mean()

    # 그래프 상단에 평균값 표시
    ax.text(0.5, 0.95, f'Average: {mean_speed:.2f}', transform=ax.transAxes, 
            ha='center', va='top', bbox=dict(facecolor='white', edgecolor='black'))

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

for video_id, group_data in grouped:
    # stride 데이터 그래프 생성 및 표시
    fig_stride, ax_stride = plt.subplots(figsize=(8, 4))
    ax_stride.plot(group_data['stride_index'], group_data['stride'], label='stride')
    ax_stride.set_title(f'Stride for Video ID {video_id}')
    ax_stride.set_xlabel('Index')
    ax_stride.set_ylabel('Stride')

    # 평균값 계산 및 표시
    mean_stride = group_data['stride'].mean()
    ax_stride.text(0.5, 0.95, f"Average: {mean_stride:.2f}", transform=ax_stride.transAxes, 
                   ha='center', va='top', bbox=dict(facecolor='white', edgecolor='black'))

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

    # 평균값 계산 및 표시
    mean_cadence = group_data['cadence'].mean()
    ax_cadence.text(0.5, 0.95, f"Average: {mean_cadence:.2f}", transform=ax_cadence.transAxes, 
                    ha='center', va='top', bbox=dict(facecolor='white', edgecolor='black'))

    ax_cadence.legend()
    plt.tight_layout()
    st.pyplot(fig_cadence)
    plt.close(fig_cadence)    

# CSV 파일 로드
csv_file = selected_data['keypoints_csv_file'].values[0]
df_keypoints = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Keypoints Data Trends')

# 데이터프레임 그룹화
grouped = df_keypoints.groupby('video_id')

columns_to_plot = [
    'angles_left_leg_up', 'angles_right_leg_up', 'angles_core_decline'
]

# 각 그룹에 대한 그래프 그리기
for video_id, group_data in grouped:
    # 컬럼별로 그래프 생성 및 표시
    for column in columns_to_plot:
        fig, ax = plt.subplots(figsize=(8, 4))
        # fig, ax = plt.subplots(figsize=(8, 5.15))  # 높이를 15% 정도 늘림
        ax.plot(group_data[column], label=column)  # 해당 컬럼의 그래프 추가
        ax.set_title(f'{column} for Video ID {video_id}')
        ax.set_xlabel('Index')
        ax.set_ylabel(column)
        ax.legend()

        # 해당 컬럼의 평균값 계산
        average_value = round(np.mean(group_data[column]), 2)

        # 그래프 상단에 평균값 표시
        ax.text(0.5, 0.95, f'Average: {average_value}', transform=ax.transAxes, 
                ha='center', va='top', bbox=dict(facecolor='white', edgecolor='black'))

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)