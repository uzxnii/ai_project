import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="wide"
)

st.title("🌍 국가별 MBTI 비율 분석")

# CSV 파일 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택
countries = sorted(df["Country"].unique())
selected_country = st.selectbox(
    "국가를 선택하세요",
    countries
)

# 선택 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 컬럼 추출
mbti_cols = [col for col in df.columns if col != "Country"]

# 값 가져오기
values = country_data[mbti_cols]

# 높은 순 정렬
values = values.sort_values(ascending=False)

# 색상 설정
top_color = "#FFD700"  # 1등 노란색

# 하늘색 → 매우 연한 하늘색 그라데이션
cmap = LinearSegmentedColormap.from_list(
    "sky_gradient",
    ["#87CEEB", "#F5FCFF"]
)

# 나머지 색상 생성
other_colors = [
    cmap(i / (len(values) - 2))
    for i in range(len(values) - 1)
]

# 전체 색상
colors = [top_color] + other_colors

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    values.index,
    values.values,
    color=colors
)

# 제목 및 라벨
ax.set_title(
    f"{selected_country}의 MBTI 비율",
    fontsize=20
)

ax.set_xlabel("MBTI 유형")
ax.set_ylabel("비율")

# x축 회전
plt.xticks(rotation=45)

# 값 표시
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

# 스트림릿 출력
st.pyplot(fig)

# 데이터 테이블
st.subheader("📊 상세 데이터")

table_df = pd.DataFrame({
    "MBTI": values.index,
    "비율": values.values
})

st.dataframe(
    table_df,
    use_container_width=True
)
