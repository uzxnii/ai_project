import streamlit as st
st.title('나의 첫 웹사이트 만들기!')
a=st.text_input('이름을 입력하세요')
b=st.selectbox('좋아하는 음식을 선택하세요',['떡볶이','마라탕','요아정'])
if st.button('인사말 생성'):
  st.write(a+'하이!!')
