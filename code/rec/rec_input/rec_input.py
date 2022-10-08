from os import write
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

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
	st.header("제주도에서 동서남북 중 어디 권역을 갈 계획인가요?")
	direction = st.multiselect('가고싶은 곳 모두 선택해주세요', jeju_df[0])
	for _ in range(0, len(direction)):
		jeju_region = jeju_df.loc[jeju_df[0] == direction[_]][1].reset_index().drop(columns=['index'])
		# st.write(jeju_region)
		jeju_select = st.multiselect('구체적인 계획이 있다면, 세부적인 여행 지역도 골라보실래요?', jeju_region[1][0])
		# st.write('You selected:', jeju_select)
	# [TODO] node 들의 특성에 대한 filtering

# traffic
def move():
	st.header("제주도에서 어떻게 이동하실건가요?")
	traffic = st.radio("하나만 선택해주세요", ["자동차", "대중교통"])
	# [TODO] 친환경적인 차 ~~는 어떠세요? - based on cakc/traffic()
	# 

# velocity

def v():
	st.header("얼마나 빡세게 제주도를 여행하시나요?")
	select = st.selectbox("하나만 선택해주세요", ["빡빡하게", "여유롭게"])
	pass

# hexagon


def radar_chart(val1, val2, val3, val4, val5):
    df = pd.DataFrame(dict(
        r=[val1, val2, val3, val4, val5],
        theta=['자연', '액티비티', '핫플레이스', '유명 관광지', '힐링'])
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
	val1, val2, val3, val4, val5 = st.slider('Select value', 0, 10, 1, key='val1'), st.slider('Select value', 0, 10, 1, key='val2'), st.slider('Select value', 1, 10, 1, key='val3'), st.slider('Select value', 0, 10, 1, key='val4'), st.slider('Select value', 0, 10, 1, key='val5')
	radar_chart(val1, val2, val3, val4, val5)

def main():
	st.title("[여행지] Input")
	direc()
	v()
	move()
	prop()


if __name__ == '__main__':
	main()
