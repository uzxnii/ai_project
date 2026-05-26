import streamlit as st
import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 페이지 설정
st.set_page_config(
    page_title="MBTI 국가 분석",
    layout="wide"
)

st.title("🌍 국가별 MBTI 분석")

# 데이터 로드
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼
mbti_cols = [col for col in df.columns if col != "Country"]

# -----------------------------
# 1. 국가별 MBTI 분석
# -----------------------------
st.header("📊 국가별 MBTI 비율")

countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가 선택",
    countries
)

# 선택 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

values = country_data[mbti_cols]

# 내림차순 정렬
values = values.sort_values(ascending=False)

# 색상 설정
top_color = "#FFD700"  # 1등 노란색

# 하늘색 그라데이션
cmap = LinearSegmentedColormap.from_list(
    "sky_gradient",
    ["#87CEEB", "#F5FCFF"]
)

other_colors = [
    cmap(i / (len(values)-2))
    for i in range(len(values)-1)
]

colors = [top_color] + other_colors

# 그래프
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    values.index,
    values.values,
    color=colors
)

ax.set_title(
    f"{selected_country}의 MBTI 비율",
    fontsize=20
)

ax.set_xlabel("MBTI")
ax.set_ylabel("비율")

plt.xticks(rotation=45)

# 값 표시
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

st.pyplot(fig)

# 데이터 테이블
st.dataframe(
    pd.DataFrame({
        "MBTI": values.index,
        "비율": values.values
    }),
    use_container_width=True
)

# -----------------------------
# 2. MBTI별 국가 TOP 10
# -----------------------------
st.header("🏆 MBTI 유형별 국가 TOP 10")

selected_mbti = st.selectbox(
    "MBTI 선택",
    mbti_cols
)

# TOP10 국가 추출
top10 = df.sort_values(
    by=selected_mbti,
    ascending=False
).head(10)

# 초록색 그라데이션
green_cmap = LinearSegmentedColormap.from_list(
    "green_gradient",
    ["#1B5E20", "#A5D6A7"]
)

top_green = "#0B6623"

green_colors = [top_green] + [
    green_cmap(i / 8)
    for i in range(9)
]

# 그래프
fig2, ax2 = plt.subplots(figsize=(12, 6))

bars2 = ax2.bar(
    top10["Country"],
    top10[selected_mbti],
    color=green_colors
)

ax2.set_title(
    f"{selected_mbti} 비율이 높은 국가 TOP 10",
    fontsize=20
)

ax2.set_xlabel("국가")
ax2.set_ylabel("비율")

plt.xticks(rotation=45)

# 값 표시
for bar in bars2:
    height = bar.get_height()

    ax2.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

st.pyplot(fig2)

# TOP10 데이터 표시
st.dataframe(
    top10[["Country", selected_mbti]]
    .reset_index(drop=True),
    use_container_width=True
)
