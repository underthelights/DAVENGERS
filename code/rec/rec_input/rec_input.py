from os import write
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

jeju_dic = {
	"동쪽": ["구좌읍", "표선면", "성산읍"],
	"서쪽": ["안덕면", "한림읍", "한경면", "대정읍"],
	"남쪽": ["중문", "서귀포", "남원읍"],
	"북쪽": ["제주시", "조천읍", "애월읍"]
}

jeju_df = pd.DataFrame(list(jeju_dic.items()))

# direction :
def direc():
	# st.write(jeju_df)
	
	direction = st.multiselect('동/서/남/북 중 가고 싶은 권역 모두 선택해주세요', jeju_df[0])
	for _ in range(0, len(direction)):
		jeju_region = jeju_df.loc[jeju_df[0] == direction[_]][1].reset_index().drop(columns=['index'])
		# st.write(jeju_region)
		jeju_select = st.multiselect('{}에서 구체적인 계획이 있다면, 세부적인 여행 지역도 골라보실래요?'.format(direction[_]), jeju_region[1][0])
		# st.write('You selected:', jeju_select)
	# [TODO] node 들의 특성에 대한 filtering

# traffic -> 
def move():
	st.subheader("제주도에서 어떻게 이동하실건가요?")
	traffic = st.radio("교통수단 하나만 선택해주세요", ["🚗 자동차", "🚌 대중교통"])
	st.info("💡 연비가 좋고 전기차일수록 탄소 배출량이 적어요")

# hexagon
def radar_chart(val1, val2, val3, val4, val5, val6):
    df = pd.DataFrame(dict(
        r=[val1, val2, val3, val4, val5, val6],
        theta=['🌳 자연', '🏛️ 문화 유적지', '🍔 맛집 추구', '🌇 핫플레이스 지수', '🗽 여행 밀도', '🏊 액티비티'])
    )

	
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
# fig.update_layout(polar=dict(radialaxis=dict(visible=True),),showlegend=False)
# fig.update_traces(fill='toself')
# fig.update_traces(fill='toself')
# fig.show()
    st.write(fig)

# hexagon - color extraction


def color_ext():
	pass

def prop():
	col1, col2, col3 = st.columns(3)
	col4, col5, col6 = st.columns(3)

	# '자연', '문화 유적지', '맛집 추구', '핫플레이스 지수', '여행 밀도', '액티비티'
	col1.write('1️⃣ **🌳 자연**')
	val1 = col1.slider(' 자연관람 활동이 많아져야 탄소배출량이 적어져요! 5이상의 값을 선택해주세요💗',1, 10, 1, key='val1')
	col2.write('2️⃣ **🏛️ 문화 유적지**')
	val2 = col2.slider('제주의 문화를 알고 싶어요', 1, 10, 1, key='val2')
	col3.write('3️⃣ **🏊 액티비티**')
	val6 = col3.slider('제주를 역동적으로 즐기고 싶어요', 1, 10, 1, key='val6')
	col4.write('4️⃣ **🌇 핫플레이스 지수**')
	val4 = col4.slider('핫플이 빠지면 파티가 아니지', 1, 10, 1, key='val4')
	col5.write('5️⃣ **🗽 여행 밀도**')
	val5 = col5.slider('많은 여행지를 돌아다니면 이동할 때 드는 탄소배출량이 많이 발생하게 돼요ㅠㅠ 5이하의 값을 선택해주세요💗', 1, 10, 1, key='val5')
	col6.write('6️⃣ **🍔 맛집**')
	val3 = col6.slider('인기 있는 맛집을 찾아다니는 편인가요?', 1, 10, 1, key='val3')

	st.subheader("취향 저격 Hexagon")
	radar_chart(val1, val2, val3, val4, val5, val6)

def main():
	st.title("여행 루트 🏝️ 취향 저격 Hexagon ⬣")
	st.subheader("🧭 제주도의 어디 권역을 갈 계획인가요?")
	direc()
	move()
	st.subheader("어떤 스타일의 여행을 할 계획인가요?")
	prop()

if __name__ == '__main__':
	main()
