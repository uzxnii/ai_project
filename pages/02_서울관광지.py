import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 인기 관광지 TOP10",
    layout="wide"
)

st.title("🇰🇷 외국인이 좋아하는 서울 관광지 TOP10")
st.write("서울의 대표 관광지를 지도에서 확인해보세요!")

# 관광지 데이터
tourist_spots = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대 대표 궁궐",
        "station": "경복궁역 (3호선)",
        "detail": """
- 한복을 입고 궁궐 내부를 산책하며 한국 전통문화를 체험할 수 있습니다.
- 근처 서촌에는 감성 카페와 전통 한식 맛집이 많아 외국인 관광객에게 인기가 높습니다.
- 광화문과 청와대 거리까지 함께 둘러보며 서울의 역사적인 분위기를 즐길 수 있습니다.
"""
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리",
        "station": "안국역 (3호선)",
        "detail": """
- 한국 전통 한옥 골목길을 걸으며 사진 촬영을 즐기기 좋은 장소입니다.
- 주변 공방에서 도자기·한지 공예 체험도 가능합니다.
- 인사동과 가까워 전통 기념품 쇼핑과 길거리 음식도 함께 즐길 수 있습니다.
"""
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 먹거리 중심지",
        "station": "명동역 (4호선)",
        "detail": """
- K-뷰티 쇼핑과 다양한 패션 브랜드를 한곳에서 즐길 수 있습니다.
- 길거리 음식이 유명하며 밤에도 활기찬 분위기를 느낄 수 있습니다.
- 주변 남산서울타워와 롯데백화점까지 함께 관광하기 좋습니다.
"""
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소",
        "station": "명동역 (4호선)",
        "detail": """
- 서울 시내를 한눈에 볼 수 있는 대표 야경 명소입니다.
- 케이블카와 산책로를 이용해 남산 자연 풍경도 즐길 수 있습니다.
- 사랑의 자물쇠 포토존은 외국인 커플 관광객에게 특히 인기입니다.
"""
    },
    {
        "name": "홍대거리",
        "lat": 37.556350,
        "lon": 126.922672,
        "desc": "젊음과 예술의 거리",
        "station": "홍대입구역 (2호선)",
        "detail": """
- 버스킹 공연과 스트릿 문화가 활발한 서울 대표 핫플레이스입니다.
- 감성 카페, 클럽, 맛집이 많아 밤 늦게까지 즐길 수 있습니다.
- 젊은 예술가들의 소품샵과 개성 있는 편집샵 구경도 재미 요소입니다.
"""
    },
    {
        "name": "강남역",
        "lat": 37.497942,
        "lon": 127.027621,
        "desc": "서울 대표 번화가",
        "station": "강남역 (2호선)",
        "detail": """
- 최신 트렌드의 쇼핑몰과 레스토랑이 밀집한 지역입니다.
- 다양한 K-POP 관련 체험 공간과 포토존을 만날 수 있습니다.
- 밤에는 화려한 네온사인과 강남의 도시 분위기를 즐기기 좋습니다.
"""
    },
    {
        "name": "롯데월드타워",
        "lat": 37.512500,
        "lon": 127.102778,
        "desc": "서울 랜드마크 초고층 빌딩",
        "station": "잠실역 (2호선)",
        "detail": """
- 서울스카이 전망대에서 서울 전경을 감상할 수 있습니다.
- 롯데월드몰과 아쿠아리움, 테마파크를 함께 이용할 수 있습니다.
- 쇼핑과 엔터테인먼트를 동시에 즐기기 좋은 복합 관광지입니다.
"""
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "현대적 건축과 패션 중심지",
        "station": "동대문역사문화공원역",
        "detail": """
- 미래적인 건축 디자인으로 유명한 서울 대표 랜드마크입니다.
- 야간 조명이 아름다워 사진 촬영 명소로 유명합니다.
- 근처 동대문 쇼핑타운에서 새벽 쇼핑도 즐길 수 있습니다.
"""
    },
    {
        "name": "광장시장",
        "lat": 37.570435,
        "lon": 126.999558,
        "desc": "한국 전통시장과 길거리 음식",
        "station": "종로5가역 (1호선)",
        "detail": """
- 빈대떡, 마약김밥 등 한국 전통 먹거리를 맛볼 수 있습니다.
- 외국인 관광객들에게 한국 시장 문화를 체험하기 좋은 장소입니다.
- 주변 청계천 산책과 종로 거리 관광도 함께 추천됩니다.
"""
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "desc": "쇼핑·전시·스타필드 도서관",
        "station": "삼성역 (2호선)",
        "detail": """
- 스타필드 별마당도서관은 외국인 관광객들의 인기 포토존입니다.
- 대형 쇼핑몰과 전시장이 연결되어 있어 하루 종일 즐길 수 있습니다.
- 봉은사와 함께 방문하면 전통과 현대 분위기를 동시에 경험할 수 있습니다.
"""
    }
]

# 서울 중심 지도
seoul_center = [37.5665, 126.9780]

# 컬러 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="CartoDB positron"
)

# 파란색 마커 추가
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
            color="blue",
            icon="info-sign"
        )
    ).add_to(m)

# 지도 크기 축소 (약 80%)
st_folium(
    m,
    width=950,
    height=600
)

st.divider()

# 관광지 선택
spot_names = [spot["name"] for spot in tourist_spots]

selected_spot = st.selectbox(
    "📍 관광지를 선택하세요",
    spot_names
)

# 선택된 관광지 정보 출력
for spot in tourist_spots:
    if spot["name"] == selected_spot:

        st.subheader(f"✨ {spot['name']}")

        st.markdown(f"### 🚉 가까운 지하철역")
        st.info(spot["station"])

        st.markdown("### 🎡 주변 놀거리 및 추천 포인트")
        st.write(spot["detail"])

        break
