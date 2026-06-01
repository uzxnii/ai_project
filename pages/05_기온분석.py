import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")
    df["날짜"] = pd.to_datetime(
    df["날짜"],
    errors="coerce"
)

df = df.dropna(subset=["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

st.title("🌡️ 서울 기온 변화 분석")

month = st.sidebar.selectbox("월", range(1, 13))
day = st.sidebar.selectbox("일", range(1, 32))

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].sort_values("연도")

if filtered.empty:
    st.warning("데이터가 없습니다.")
else:

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        filtered["연도"],
        filtered["최고기온(℃)"],
        color="hotpink",
        marker="o",
        linewidth=2,
        label="최고기온"
    )

    ax.plot(
        filtered["연도"],
        filtered["최저기온(℃)"],
        color="lightblue",
        marker="o",
        linewidth=2,
        label="최저기온"
    )

    ax.set_title(f"{month}월 {day}일 연도별 기온 변화")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ],
        use_container_width=True
    )
