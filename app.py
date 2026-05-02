import streamlit as st

import random

st.set_page_config(page_title="KEIBA AI PRO", page_icon="🐎")

st.title("🐎 KEIBA AI PRO")

st.subheader("AI競馬予想システム")

# 入力

horse = st.text_input("馬名")

odds = st.number_input("単勝オッズ", min_value=1.0, value=5.0)

st.header("📊 AI分析項目")

speed = st.slider("スピード指数", 0, 100, 70)

stamina = st.slider("スタミナ指数", 0, 100, 65)

jockey = st.slider("騎手評価", 0, 100, 75)

track = st.slider("馬場適性", 0, 100, 60)

distance = st.slider("距離適性", 0, 100, 70)

form = st.slider("近走状態", 0, 100, 68)

if st.button("AI予想開始"):

    # AIスコア

    ai_score = round(

        (speed + stamina + jockey + track + distance + form) / 6,

        1

    )

    # 勝率計算

    win_rate = round(ai_score / 100 * 45, 1)

    # 複勝率

    place_rate = round(ai_score / 100 * 75, 1)

    # 期待値

    value = round((ai_score / odds), 2)

    st.header("📈 AI総合評価")

    st.metric("AIスコア", ai_score)

    st.metric("勝率", f"{win_rate}%")

    st.metric("複勝率", f"{place_rate}%")

    st.metric("期待値", value)

    # 評価

    if value >= 15:

        st.success("🔥 超期待値馬")

    elif value >= 10:

        st.info("✅ 狙い目")

    else:

        st.warning("⚠ 人気先行")

    # 券種別予想

    st.header("🎯 券種別AI予想")

    st.write(f"🥇 単勝：{horse}")

    st.write(f"🥈 複勝：{horse}")

    st.write(f"🎯 ワイド：{horse} - 穴馬候補")

    st.write(f"🎯 馬連：{horse} - 対抗馬")

    st.write(f"🎯 馬単：{horse} → 対抗馬")

    st.write(f"🔥 3連複：{horse} - 対抗馬 - 穴馬")

    st.write(f"🔥 3連単：{horse} → 対抗馬 → 穴馬")

    # AIコメント

    comments = [

        f"{horse}は展開次第で好走可能。",

        f"{horse}は騎手評価が高く期待。",

        f"{horse}は穴馬として面白い存在。",

        f"{horse}は安定感が高い。",

        f"{horse}は高配当演出の可能性あり。",

    ]

    st.header("🤖 AIコメント")

    st.write(random.choice(comments))

    # 最終評価

    st.header("🏆 AI最終判定")

    if ai_score >= 80:

        st.success("S評価 ★ 激アツ")

    elif ai_score >= 70:

        st.info("A評価 ★ 有力")

    elif ai_score >= 60:

        st.warning("B評価 ★ 注意")

    else:

        st.error("C評価 ★ 厳しい")

st.divider()

st.caption("KEIBA AI PRO SYSTEM")
