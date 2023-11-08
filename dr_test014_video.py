import os
import streamlit as st

# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.sidebar.selectbox('Select a video file', filenames)
#     return os.path.join(folder_path, selected_filename)

# def main():
#     filename = file_selector("/Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/result_6angles230817_2_h264_codec.mp4")
#     if st.button("Play video"):
#         video_file = open(filename, 'rb')
#         video_bytes = video_file.read()
#         st.video(video_bytes)

# if __name__ == '__main__':
#     main()

# ## play video로 성공!!
# filename = "/Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/result_6angles230817_2_h264_codec.mp4"
# if st.button("Play video"):
#     video_file = open(filename, 'rb')
#     video_bytes = video_file.read()
#     st.video(video_bytes)

## play video로 성공!!
filename = "/Users/jasper0325/Documents/workspace/codes/streamlit_dr_deploy/result_6angles230817_2_h264_codec.mp4"

video_file = open(filename, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)