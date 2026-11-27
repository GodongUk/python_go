import streamlit as st

st.set_page_config(page_title="학습 안내", layout="wide")
st.title("글러브 판매 사이트",)
st.markdown("글러브 판매 관련 사이트 입니다.")
st.sidebar.header("광고 제목")
st.sidebar.write("광고 내용")
left, right = st.columns(2)
with left:
    st.header("미즈노 글러브")
    st.write("미즈노 글러브는 어쩌구 저쩌구")
with right:
    st.header("등급별 가격 안내")
    st.write("미즈노 프로")
    st.write("700,000")
    st.write("미즈노 A에디션")
    st.write("500,000")