import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP10",
    layout="wide"
)

st.title("🇰🇷 외국인이 좋아하는 서울 관광지 TOP10")
st.write("폴리움(Folium) 지도로 서울의 대표 관광지를 표시합니다.")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 관광지 데이터
tourist_spots = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대 대표 궁궐"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 먹거리 중심지"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "홍대거리",
        "lat": 37.556350,
        "lon": 126.922672,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "강남역",
        "lat": 37.497942,
        "lon": 127.027621,
        "desc": "서울 대표 번화가"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.512500,
        "lon": 127.102778,
        "desc": "서울 랜드마크 초고층 빌딩"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "현대적 건축과 패션 중심지"
    },
    {
        "name": "광장시장",
        "lat": 37.570435,
        "lon": 126.999558,
        "desc": "한국 전통시장과 길거리 음식"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "desc": "쇼핑·전시·스타필드 도서관"
    }
]

# 마커 추가
for idx, spot in enumerate(tourist_spots, start=1):
    popup_text = f"""
    <b>TOP {idx}. {spot['name']}</b><br>
    {spot['desc']}
    """

    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=spot["name"],
        icon=folium.Icon(
            color="red",
            icon="info-sign"
        )
    ).add_to(m)

# 지도 출력
st_folium(
    m,
    width=1200,
    height=700
)

# 관광지 리스트 출력
st.subheader("📍 관광지 목록")

for idx, spot in enumerate(tourist_spots, start=1):
    st.markdown(
        f"**TOP {idx}. {spot['name']}** - {spot['desc']}"
    )
