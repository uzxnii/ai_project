from pathlib import Path

app_code = r'''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.set_page_config(page_title="서울 인구 연령별 분석", layout="wide")

st.title("서울 행정구별 연령별 인구 분석")

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv("population.csv", encoding="cp949")

# 행정구 이름 정리
df["행정구명"] = df["행정구역"].str.split("(").str[0].str.strip()

# 2026년 4월 기준 연령 컬럼 추출
age_columns = [col for col in df.columns if "2026년04월_거주자_" in col and "세" in col]

# 나이 추출
ages = []
for col in age_columns:
    age_text = col.split("_")[-1].replace("세", "")
    
    if "100세 이상" in col:
        ages.append(100)
    else:
        ages.append(int(age_text))

# 행정구 선택
districts = df["행정구명"].tolist()
selected_district = st.selectbox("행정구를 선택하세요", districts)

# 선택 데이터
selected_row = df[df["행정구명"] == selected_district].iloc[0]

# 인구 데이터 정리
population = []
for col in age_columns:
    value = str(selected_row[col]).replace(",", "")
    population.append(int(value))

# 그래프 생성
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color="hotpink",
    linewidth=3
)

# 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))
ax.grid(axis="x", linestyle="--", alpha=0.5)

# 제목 및 축 라벨
ax.set_title(f"{selected_district} 연령별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)

st.pyplot(fig)

st.caption("데이터 기준: 2026년 4월 서울시 거주자 인구 데이터")
'''

requirements_code = """streamlit
pandas
matplotlib
"""

base = Path("/mnt/data")

(app_path := base / "app.py").write_text(app_code, encoding="utf-8")
(req_path := base / "requirements.txt").write_text(requirements_code, encoding="utf-8")

print(f"생성 완료: {app_path}")
print(f"생성 완료: {req_path}")
