import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 데이터 로드
file_path = '/mnt/data/age2411.csv'
data = pd.read_csv(file_path)

# 데이터 전처리: 필요한 열 추출 및 이름 정리
data = data[['행정구역', '2024년11월_계_총인구수', '2024년11월_계_연령구간인구수',
             '2024년11월_남_총인구수', '2024년11월_여_총인구수']]
data.columns = ['지역', '총인구수', '연령구간인구수', '남성인구수', '여성인구수']

# Streamlit 앱
st.title("📊 지역별 남녀 성별 인구 그래프")
st.sidebar.header("지역 선택")
selected_region = st.sidebar.selectbox("지역을 선택하세요:", data['지역'].unique())

# 선택한 지역 데이터 필터링
filtered_data = data[data['지역'] == selected_region]

if not filtered_data.empty:
    # 그래프 생성
    st.subheader(f"선택한 지역: {selected_region}")
    st.write(f"총인구수: {filtered_data['총인구수'].values[0]:,}명")
    
    fig, ax = plt.subplots()
    ax.bar(['남성', '여성'], [filtered_data['남성인구수'].values[0], filtered_data['여성인구수'].values[0]],
           color=['blue', 'pink'])
    ax.set_ylabel("인구수")
    ax.set_title(f"{selected_region} 남녀 성별 인구")
    
    # 그래프 표시
    st.pyplot(fig)
else:
    st.error("해당 지역에 대한 데이터가 없습니다.")

