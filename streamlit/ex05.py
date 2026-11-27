import streamlit as st
st.title("구매 금액 계산")


price = st.number_input("단가", min_value=2000, max_value=50000, value=3000)

numberStr = st.number_input("수량", min_value=1, max_value=50, value=1)

total = int(price) * int(numberStr)
st.metric("총액", f"{total:,}원")

totalsum = int(price) + int(numberStr)
st.metric("더하기", f"{totalsum:,}원")

totalminus = int(price) - int(numberStr)
st.metric("빼기", f"{totalminus:,}원")

totalnanugi = int(price) / int(numberStr)
st.metric("나누기", f"{totalnanugi:,}원")