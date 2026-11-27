import streamlit as st
st.title("질문 길이 알려 주는 응답")
if "messages" not in st.session_state:
    st.session_state.messages = []
if st.button("대화 지우기"):
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
question = st.chat_input("질문을 입력하세요")
if question and question.strip():
    answer = f"연습 응답: {question.strip()}"
    for role, content in [("user", question),("assistant", answer) ,("user", len(question))]:
        st.session_state.messages.append({"role":role, "content":content})
    st.session_state.messages = st.session_state.messages[-10:]

    # st.rerun()
    #     with st.chat_message(role):
    #         st.write(content) 