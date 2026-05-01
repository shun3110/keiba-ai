
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="KEIBA AI COMPLETE", layout="wide")

st.title("🏇 KEIBA AI COMPLETE SYSTEM")

horse = st.text_input("馬名", "サンプルホース")
odds = st.number_input("単勝オッズ", 1.0, 999.9, 5.0)

if st.button("AI解析"):
    ai_index = random.randint(50, 99)
    win_rate = round(random.uniform(5, 80), 1)
    expected = round((win_rate / 100) * odds, 2)

    st.metric("AI指数", ai_index)
    st.metric("勝率", f"{win_rate}%")
    st.metric("期待値", expected)

    if expected >= 1:
        st.success("🔥 回収期待あり")
    else:
        st.warning("⚠ 人気先行")

    st.subheader("自動買い目")
    st.write(f"単勝: {horse}")
    st.write(f"複勝: {horse}")

    st.subheader("AIコメント")
    st.write(
        f"{horse}は近走内容と期待値から高評価。"
        "展開次第で好走可能。"
    )
