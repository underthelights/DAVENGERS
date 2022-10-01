from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd

st.title("[탄소 발자국 계산기] 음식")
carbon_store_avg , carbon_store_food, carbon_food_category, carbon_food_igrd = 0,0,0,0

def store():
	global carbon_store_avg , carbon_store_food
	# [TODO?] 제주시, 서귀포시 중 어디에 위치하나요? -> 네이버 구 주소 크롤링, 시/군까지?
	
	select_option_store = st.radio("이용하신 가게를 저희 데이터에서 찾아보시겠어요?", ("네, 찾아볼게요", "데이터베이스에 없어요"))

	if select_option_store == "네, 찾아볼게요":
		food_menu = pd.read_csv('data/preprocessed/food/food_menu.csv')
		option_store = st.selectbox('가게 상호명', (food_menu['MCT_NM'].unique()))
		option_menu = (food_menu.loc[(food_menu['MCT_NM'] == option_store)])['menu_list']
		# st.write(option_menu[0].split(', '))
		option_menu = option_menu[0].split(', ')
		option_menu_select = st.selectbox('어떤 메뉴를 드셨나요?', (option_menu))
		# [TODO] 혜나 category 정해지면 카테고리 별 연산, + t1

		st.write("해당 음식점의 평균 탄소배출량은 {}kgCO2입니다.".format(carbon_store_avg))
		st.write("음식을 드시면서 배출하신 탄소량은 {}kgCO2 이에요".format(carbon_store_food))

	elif select_option_store == "데이터베이스에 없어요":
		st.write("저희 데이터베이스에 있는 식당이 아닙니다")	
		select_option_food = st.radio("음식 메뉴로 탄소 발자국을 계산하실래요?", ("네, 좋아요", "아니요, 괜찮아요"))
		if select_option_food == "네, 좋아요":
			food()
		elif select_option_food == "아니요, 괜찮아요":
			st.write("END")
	
def food():
	global carbon_food_category
	select_option_store = st.radio("음식을 드셨나요", ("네, 먹었어요", "아니요, 아무것도 안 먹었어요"))
	if select_option_store == "네, 먹었어요":
		food_menu = pd.read_csv('data/preprocessed/food/food_menu.csv')
		# st.write(food_menu)
		option_store = st.selectbox('드신 음식의 분류를 알려주세요.', (food_menu['menu_list'].unique())) # [TODO] 'MENU' Category 명명 다시

		st.write("음식을 드시면서 배출하신 탄소량은 {}kgCO2 이에요".format(carbon_food_category))

	elif select_option_store == "아니요, 아무것도 안 먹었어요":
		st.write("배출하신 탄소량은 0kgCO2 이에요")

def ingredient():
	global carbon_food_igrd
	select_option_store = st.radio("음식을 드셨나요", ("네, 먹었어요", "아니요, 아무것도 안 먹었어요"))
	if select_option_store == "네, 먹었어요":

		igrd = pd.read_csv('data/preprocessed/food/food_revised.csv')
		option_food_type = st.multiselect('드신 음식의 분류를 알려주세요.', (igrd['type_detail'].unique()))
		#[TODO] 한국어로 reindex화 진행
		for _ in range(0, len(option_food_type)):
			carbon_food_df = pd.DataFrame(igrd.loc[igrd['type_detail'] == option_food_type[_]])['CO2']
			# st.write(carbon_food_df.unique()[0])
			carbon_food_igrd += carbon_food_df.unique()[0]
		st.write("음식을 드시면서 배출하신 탄소량은 {}kgCO2 이에요".format(carbon_food_igrd))

	elif select_option_store == "아니요, 아무것도 안 먹었어요":
		st.write("배출하신 탄소량은 0kgCO2 이에요")


def main():
	checkbox_store = st.checkbox("(Q1) 제주도에서 어떤 음식점에 가셨나요?")
	checkbox_food = st.checkbox("(Q2) 제주도에서 어떤 음식을 드셨나요?")
	checkbox_ingredient = st.checkbox("(Q3) 제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")

	if checkbox_store:
		store()
	if checkbox_food:
		food()
	if checkbox_ingredient:
		ingredient()

	# st.success('여행에서 나온 총 탄소 배출량은 {}kgCO2 입니다'.format(carbon_sum_co2+carbon_sum_traffic))
	# st.write('(Q1) 탄소 배출량은 ', carbon_sum_traffic, 'kgCO2 입니다')
	# st.write('(Q2) 탄소 배출량은 ', carbon_sum_co2, 'kgCO2 입니다')
	
if __name__ == '__main__':
	main()