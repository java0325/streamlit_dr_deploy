import pandas as pd
import streamlit as st

# CSV 파일 경로 설정
file_path = 'dr_rec002.csv'
# CSV 파일을 'cp949' 또는 'euc-kr' 인코딩으로 읽기
df = pd.read_csv(file_path, encoding='cp949')  # 또는 encoding='euc-kr'

# Streamlit 애플리케이션 시작
st.title('영상 분석 결과')

# Sidebar에 날짜 선택 옵션 추가
selected_date = st.sidebar.selectbox('훈련 기록을 선택하세요👏', df['date'])

# 선택한 날짜에 해당하는 데이터 추출
selected_data = df[df['date'] == selected_date]

# 선택한 날짜에 대한 데이터 표시
st.write(f"### 분석 결과: {selected_date}")
st.table(selected_data[['place', 'company', 'runner_name', ]])
# st.table(selected_data[['place', 'company', 'runner_name', 'avg_speed', 'current_speed', 'stride', 'steps']])

from PIL import Image

# # 이미지 로딩 및 표시
# image = Image.open('runner001.png')
# st.image(image, use_column_width=True)

# # 'avg_speed', 'current_speed', 'stride', 'steps' 데이터 값 표시
# st.write('Average Speed:', df['avg_speed'][0])
# st.write('Current Speed:', df['current_speed'][0])
# st.write('Stride:', df['stride'][0])
# st.write('Steps:', df['steps'][0])

# 이미지 로딩 및 데이터 값 표시를 같은 행에 배치
col1, col2 = st.columns(2)  # 2개의 컬럼 생성

# 첫 번째 컬럼에 이미지 표시
with col1:
    image = Image.open('runner001.png')
    st.image(image, use_column_width=True)

# # 첫 번째 컬럼에 이미지 표시 (너비 조절)
# with col1:
#     image = Image.open('runner001.png')
#     st.image(image, width=400)  # 이미지의 너비를 400 픽셀로 설정    

# 두 번째 컬럼에 데이터 값 표시
with col2:
    st.write('Average Speed:', df['avg_speed'][0])
    st.write('Current Speed:', df['current_speed'][0])
    st.write('Stride:', df['stride'][0])
    st.write('Steps:', df['steps'][0])

# # 이미지 로딩
# image = Image.open('runner001.png')

# # 좌측 컬럼에 이미지 표시 (너비 조절)
# col1, col2 = st.columns(2)  # 2개의 컬럼 생성

# with col1:
#     st.image(image, width=800)  # 이미지의 너비를 400 픽셀로 설정

# # 두 번째 컬럼에 데이터 값 표시 (우측으로 이동)
# with col2:
#     # 데이터 값을 우측으로 이동시키기 위해 스타일을 지정
#     st.write('<style>')
#     st.write('.data-values {')
#     st.write('    margin-left: 20px;')  # 20px 만큼 우측으로 이동
#     st.write('}')
#     st.write('</style>', unsafe_allow_html=True)
    
#     # 데이터 값을 출력하고 클래스를 지정하여 스타일을 적용
#     st.write('<div class="data-values">')
#     st.write('Average Speed:', df['avg_speed'][0])
#     st.write('Current Speed:', df['current_speed'][0])
#     st.write('Stride:', df['stride'][0])
#     st.write('Steps:', df['steps'][0])
#     st.write('</div>', unsafe_allow_html=True)

    # 스타일을 사용하여 우측으로 이동 (예: margin-left)
    st.write('<style>div.row-widget.stRadio > div{flex-direction: row-reverse;}</style>', unsafe_allow_html=True)

# # 데이터 프레임 표시 (header와 순번 제외)
# st.table(df[['place', 'company', 'runner_name', 'avg_speed', 'current_speed', 'stride', 'steps']].reset_index(drop=True))

# 추가적인 CSV 파일 로딩
csv_file_1 = 'dr_rec002.csv'
csv_file_2 = 'dr_rec003.csv'
csv_file_3 = 'dr_rec004.csv'

# CSV 파일을 데이터프레임으로 로딩
df_csv_1 = pd.read_csv(csv_file_1)
df_csv_2 = pd.read_csv(csv_file_2)
df_csv_3 = pd.read_csv(csv_file_3)

# 데이터프레임 표시
st.header('Additional Data from CSV Files')
st.subheader('CSV File 1')
st.write(df_csv_1)
st.subheader('CSV File 2')
st.write(df_csv_2)
st.subheader('CSV File 3')
st.write(df_csv_3)