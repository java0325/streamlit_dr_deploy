import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# CSV 파일 경로 설정
file_path = 'dr_rec002.csv'
# CSV 파일을 'cp949' 또는 'euc-kr' 인코딩으로 읽기
df = pd.read_csv(file_path, encoding='cp949')  # 또는 encoding='euc-kr'

# Streamlit 애플리케이션 시작
st.title('Video analysis results')

# Sidebar에 날짜 선택 옵션 추가
selected_date = st.sidebar.selectbox('Please choose a training date👏', df['date'])

# 선택한 날짜에 해당하는 데이터 추출
selected_data = df[df['date'] == selected_date]

# # 선택한 날짜에 대한 데이터 표시
# st.write(f"### Analysis results: {selected_date}")
# st.table(selected_data[['place', 'company', 'runner_name']])

# # 선택한 날짜에 대한 데이터 표시 (줄 번호 숨기기)
# st.write(f"### Analysis results: {selected_date}")
# st.table(selected_data[['place', 'company', 'runner_name']], index=False)

st.write(f"### Analysis results: {selected_date}")
selected_data_display = selected_data[['place', 'company', 'runner_name']]
st.table(selected_data_display)

# selected_data_display = selected_data[['place', 'company', 'runner_name']]
# st.table(selected_data_display, use_container_width=True, show_index=False)

# selected_data_display = selected_data[['Place', 'Company', 'Runner_name']].reset_index(drop=True)
# st.table(selected_data_display)

# # 인덱스를 재설정하고 "Number"라는 칼럼 이름으로 변경
# selected_data_display = selected_data[['place', 'company', 'runner_name']].reset_index(drop=True)
# selected_data_display = selected_data_display.rename(columns={'index': 'Number'})

# # 테이블로 데이터 표시
# st.table(selected_data_display, use_container_width=True)

# # 인덱스를 재설정하고 "Number"라는 칼럼 이름으로 변경
# selected_data_display = selected_data[['place', 'company', 'runner_name']].reset_index(drop=True)
# selected_data_display.columns = ['Number', 'Place', 'Company', 'Runner Name']

# # 테이블로 데이터 표시
# st.table(selected_data_display)

# # 인덱스를 재설정하고 "Number"라는 칼럼 이름으로 변경
# selected_data_display = selected_data[['place', 'company', 'runner_name']].reset_index(drop=True)
# selected_data_display.columns = ['Place', 'Company', 'Runner Name']  # "Number" 열은 삭제됩니다

# # 테이블로 데이터 표시
# st.table(selected_data_display)

# 이미지 파일 경로 가져오기
img_file = selected_data['img_file'].values[0]

# 이미지 로딩 및 데이터 값 표시를 같은 행에 배치
col1, col2 = st.columns(2)  # 2개의 컬럼 생성

# 첫 번째 컬럼에 이미지 표시
with col1:
    image = Image.open(img_file)
    st.image(image, use_column_width=True)

# 두 번째 컬럼에 데이터 값 표시
with col2:
    st.write('Average Speed:', df['avg_speed'][0])
    st.write('Current Speed:', df['current_speed'][0])
    st.write('Stride:', df['stride'][0])
    st.write('Steps:', df['steps'][0])

# CSV 파일 로드
csv_file = selected_data['record_file'].values[0]
df = pd.read_csv(csv_file)

# 그래프 표시 (동일한 행에 나열)
st.write('## Motion Data Trends')

# 각 컬럼의 데이터를 그래프로 표시
fig, ax = plt.subplots(1, 4, figsize=(15, 4))  # 1행 4열의 서브플롯 생성

# 'left hip' 데이터 그래프
ax[0].plot(df['left hip'])
ax[0].set_title('Left Hip')

# 'left knee' 데이터 그래프
ax[1].plot(df['left knee'])
ax[1].set_title('Left Knee')

# 'right hip' 데이터 그래프
ax[2].plot(df['right hip'])
ax[2].set_title('Right Hip')

# 'right knee' 데이터 그래프
ax[3].plot(df['right knee'])
ax[3].set_title('Right Knee')

# 그래프 스타일 및 레이블 설정
for i in range(4):
    ax[i].set_xlabel('Time')
    ax[i].set_ylabel('Position')

# 서브플롯 레이아웃 조정
plt.tight_layout()

# 그래프를 Streamlit 애플리케이션에 표시
st.pyplot(fig)
