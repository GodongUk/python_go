import pandas as pd
import streamlit as st

st.title("평균 점수")
rows = [
    {"subject": "국어", "score":80},
    {"subject": "수학", "score":90},
    {"subject": "영어", "score":100}
]
df = pd.DataFrame(rows)
df["평균"] = int(df["score"].sum()) / 3
st.dataframe(df, hide_index=True) #없으면 행 번호출력
#st.bar_chart(df.set_index("subject")["score"]) #[]는 배열로 착각 가능
st.bar_chart(df.set_index("subject").get("score"))
