import streamlit as st
st.title("이메일 확인")
with st.form("main_form"):
    name = st.text_input("이름")
    email = st.text_input("이메일")
    tel = st.text_input("전화번호")
    submitted = st.form_submit_button("확인하기")
    
    if submitted :
        if "@" not in email:
            st.error("이메일을 다시 확인해주세요")
        else:
            st.write(f"{name}님 이메일 {email}이 확인되었습니다.")
    if tel :
        if "010" not in tel: 
            st.error("전화번호를 다시 확인해주세요")
        else:
            st.write(f"{name}님 전화번호 {tel}이 확인되었습니다.")
    
