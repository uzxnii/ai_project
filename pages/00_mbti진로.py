import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 💼",
    page_icon="🌈",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "분석적이고 전략 세우는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 6,500만 원"
        },
        {
            "job": "🚀 AI 개발자",
            "major": "인공지능학과, 소프트웨어학과",
            "personality": "혼자 깊게 몰입하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 7,000만 원"
        }
    ],

    "INTP": [
        {
            "job": "🔬 연구원",
            "major": "물리학과, 생명과학과",
            "personality": "호기심 많고 탐구하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "job": "💻 백엔드 개발자",
            "major": "컴퓨터공학과",
            "personality": "논리적으로 문제 해결하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만 원"
        }
    ],

    "ENTJ": [
        {
            "job": "📈 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "리더십 있고 추진력이 강한 사람",
            "salary": "평균 연봉 약 7,500만 원"
        },
        {
            "job": "🏢 스타트업 CEO",
            "major": "경영학과",
            "personality": "도전 정신이 강하고 목표 지향적인 사람",
            "salary": "평균 연봉 약 8,000만 원 이상"
        }
    ],

    "ENTP": [
        {
            "job": "🎤 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "아이디어 많고 말하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "📱 콘텐츠 크리에이터",
            "major": "미디어학과",
            "personality": "창의적이고 트렌드에 민감한 사람",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],

    "INFJ": [
        {
            "job": "🧡 심리상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 배려심 많은 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "job": "📚 작가",
            "major": "문예창작학과",
            "personality": "상상력이 풍부하고 감수성이 깊은 사람",
            "salary": "평균 연봉 약 4,000만 원"
        }
    ],

    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감성적이고 창의적인 사람",
            "salary": "평균 연봉 약 4,200만 원"
        },
        {
            "job": "🎬 영상 감독",
            "major": "영화영상학과",
            "personality": "자기 표현을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 이끄는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "job": "🤝 HR 담당자",
            "major": "경영학과, 심리학과",
            "personality": "소통 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 5,200만 원"
        }
    ],

    "ENFP": [
        {
            "job": "🎭 공연 기획자",
            "major": "문화콘텐츠학과",
            "personality": "에너지 넘치고 창의적인 사람",
            "salary": "평균 연봉 약 4,800만 원"
        },
        {
            "job": "📢 광고 AE",
            "major": "광고홍보학과",
            "personality": "사람 만나는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],

    "ISTJ": [
        {
            "job": "📊 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람",
            "salary": "평균 연봉 약 7,000만 원"
        },
        {
            "job": "🏛️ 공무원",
            "major": "행정학과",
            "personality": "안정적이고 계획적인 사람",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],

    "ISFJ": [
        {
            "job": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "아이들을 좋아하는 사람",
            "salary": "평균 연봉 약 4,200만 원"
        }
    ],

    "ESTJ": [
        {
            "job": "📋 프로젝트 매니저",
            "major": "경영학과",
            "personality": "체계적이고 리더십 있는 사람",
            "salary": "평균 연봉 약 6,500만 원"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적이고 책임감 있는 사람",
            "salary": "평균 연봉 약 8,000만 원"
        }
    ],

    "ESFJ": [
        {
            "job": "💄 서비스 매니저",
            "major": "서비스경영학과",
            "personality": "친절하고 사람 챙기는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "job": "🎓 학원 강사",
            "major": "교육학과",
            "personality": "설명 잘하고 친화력 좋은 사람",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "job": "🛠️ 자동차 정비사",
            "major": "자동차공학과",
            "personality": "실전형 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],

    "ISFP": [
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "job": "🖌️ 그래픽 디자이너",
            "major": "시각디자인학과",
            "personality": "감각적이고 자유로운 사람",
            "salary": "평균 연봉 약 4,300만 원"
        }
    ],

    "ESTP": [
        {
            "job": "🏀 스포츠 마케터",
            "major": "스포츠경영학과",
            "personality": "활동적이고 도전적인 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "✈️ 승무원",
            "major": "항공서비스학과",
            "personality": "사교적이고 센스 있는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        }
    ],

    "ESFP": [
        {
            "job": "🎤 방송인",
            "major": "방송연예학과",
            "personality": "사람들 앞에 서는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "🛍️ 패션 MD",
            "major": "패션디자인학과",
            "personality": "트렌드에 민감한 사람",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ]
}

st.title("🌈 MBTI 진로 추천 프로그램")
st.write("너의 MBTI에 딱 맞는 진로를 찾아보자 😎")

mbti_list = list(mbti_data.keys())

selected_mbti = st.selectbox(
    "👉 너의 MBTI를 선택해줘!",
    mbti_list
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"{selected_mbti} 유형에게 잘 어울리는 진로야!")

    careers = mbti_data[selected_mbti]

    for career in careers:
        st.markdown("---")
        st.subheader(career["job"])
        st.write(f"📚 추천 학과 : {career['major']}")
        st.write(f"💡 잘 맞는 성격 : {career['personality']}")
        st.write(f"💰 평균 연봉 : {career['salary']}")

    st.balloons()

st.markdown("---")
st.caption("💖 재미로 보는 추천이니까 너무 진지하게만 보진 마!")
