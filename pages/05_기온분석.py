import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 기온 변화 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 특정 날짜 기온 변화")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")
    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

st.sidebar.header("날짜 선택")

month = st.sidebar.selectbox(
    "월 선택",
    range(1, 13)
)

day = st.sidebar.selectbox(
    "일 선택",
    range(1, 32)
)

# 선택한 날짜 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

st.subheader(f"📈 {month}월 {day}일의 연도별 기온 변화")

if filtered.empty:
    st.warning("해당 날짜의 데이터가 없습니다.")
else:

    fig = go.Figure()

    # 최고기온
    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최고기온(℃)"],
            mode="lines+markers",
            name="최고기온",
            line=dict(
                color="hotpink",
                width=3
            ),
            marker=dict(size=7)
        )
    )

    # 최저기온
    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최저기온(℃)"],
            mode="lines+markers",
            name="최저기온",
            line=dict(
                color="lightblue",
                width=3
            ),
            marker=dict(size=7)
        )
    )

    fig.update_layout(
        title=f"{month}월 {day}일 연도별 최고·최저기온",
        xaxis_title="연도",
        yaxis_title="기온(℃)",
        hovermode="x unified",
        template="plotly_white",
        legend_title="기온 종류",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📋 데이터")

    st.dataframe(
        filtered[
            [
                "연도",
                "최저기온(℃)",
                "최고기온(℃)"
            ]
        ],
        use_container_width=True
    )
