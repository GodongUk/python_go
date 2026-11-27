import pandas as pd
import streamlit as st

st.title("상품별 매출")
rows = [
    {"product": "book", "quantity":2, "price": 12000},
    {"product": "pen", "quantity":5, "price": 1500}
]
df = pd.DataFrame(rows)
df["revenue"] = df["quantity"] * df["price"]
st.dataframe(df, hide_index=True) #없으면 행 번호출력
st.bar_chart(df.set_index("product")["revenue"])
st.metric("총매출", f"{int(df['revenue'].sum()):,}원")
print(rows[0]["price"])
st.write(rows[0]["price"])
st.write(rows[0].get("price"))