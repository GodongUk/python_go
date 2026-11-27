import streamlit as st
st.title("숫자 5씩")
if "count" not in st.session_state:
    #st.session_state.count(min_value=0)
    st.session_state.count = 0
if st.button("증가"):
    st.session_state.count += 10
if st.button("감소"):
    #st.session_state.score = max(0, st.session_state.score - 5)
    st.session_state.count -= 5
    if st.session_state.count < 0:
        st.session_state.count = 0
if st.button("초기화"):
    st.session_state.count = 0

st.metric("현재 값", st.session_state.count)
