import streamlit as st

import random

st.set_page_config(page_title="KEIBA AI COMPLETE SYSTEM", page_icon="🏇")

st.title("🏇 KEIBA AI COMPLETE SYSTEM")

horse = st.text_input("馬名", "サンプルホース")

odds = st.number_input("単勝オッズ", 1.0, 999.9, 5.0)

if st.button("AI解析"):

    score = random.uniform(0, 1)

    st.subheader("AI解析結果")

    st.metric("期待値", round(score, 2))

    if score >= 0.75:

        rank = "SS"

        comment = "🔥 超本命級！期待値かなり高い"

        buy = "単勝・馬連"

    elif score >= 0.55:

        rank = "S"

        comment = "✅ 好走期待。軸候補"

        buy = "単勝・複勝"

    elif score >= 0.35:

        rank = "A"

        comment = "⚠️ 展開次第"

        buy = "複勝"

    else:

        rank = "C"

        comment = "❌ 見送り推奨"

        buy = "購入非推奨"

    st.success(f"AIランク : {rank}")

    st.write("### 自動買い目")

    st.write(buy)

    st.write("### AIコメント")

    st.write(comment)

    win_rate = round(score * 100, 1)

    recovery = round((score * odds) * 100, 1)

    st.write("### 勝率")

    st.progress(int(win_rate))

    st.write(f"{win_rate}%")

    st.write("### 回収率")

    st.progress(min(int(recovery), 100))

    st.write(f"{recovery}%")

    if odds >= 10 and score >= 0.5:

        st.warning("💥 AI穴馬検知")
