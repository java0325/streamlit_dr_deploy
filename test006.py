import streamlit as st
from PIL import Image

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
zarathu_img = Image.open('climbscore.png')

col1,col2 = st.columns([2,3])

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# 컬럼2에 불러온 사진 표시하기
col2.image(zarathu_img)