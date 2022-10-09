from os import write
import streamlit as st
import pandas as pd
import numpy as np

carbon_store_avg , carbon_store_food, carbon_food_category, carbon_food_igrd = 0,0,0,0

def store():
	global carbon_store_avg
	# [TODO?] 제주시, 서귀포시 중 어디에 위치하나요? -> 네이버 구 주소 크롤링, 시/군까지?
	
	select_option_store = st.radio("이용하신 식당을 저희 데이터에서 찾아보시겠어요?", ("네, 찾아볼게요", "데이터베이스에 없어요"))

	if select_option_store == "네, 찾아볼게요":
		restaurant_carbon =pd.read_csv('data/preprocessed/food/restaurant_carbon.csv')
		# st.write(restaurant_carbon)

		# food_menu = pd.read_csv('data/preprocessed/food/food_menu.csv')
		# option_store = st.selectbox('가게 상호명', (food_menu['MCT_NM'].unique()))
		# option_menu = (food_menu.loc[(food_menu['MCT_NM'] == option_store)])['menu_list']
		# # st.write(option_menu[0].split(', '))
		# option_menu = option_menu[0].split(', ')
		# option_menu_select = st.selectbox('어떤 메뉴를 드셨나요?', (option_menu))
		# # [TODO] 혜나 category 정해지면 카테고리 별 연산, + t1
		option_res_name = st.multiselect('어디 식당에서 드실 계획인가요?', (restaurant_carbon['MCT_NM'].unique()))
		option_day = 0
		for _ in range(0, len(option_res_name)):
			carbon_store_element = float((restaurant_carbon.loc[restaurant_carbon['MCT_NM'] == option_res_name[_]])['carbon_avg'])
			st.write('{}에서 발생한 탄소 배출량은 {}kgCO2입니다'.format(option_res_name[_], carbon_store_element))
			carbon_store_avg = carbon_store_avg + carbon_store_element

		st.write("식당에서 배출하신 총 탄소량은 {}kgCO2 이에요".format(carbon_store_avg))

	elif select_option_store == "데이터베이스에 없어요":
		st.warning("저희 데이터베이스에 있는 식당이 아닙니다")	
		select_option_food = st.radio("어떤 음식을 드실지 계획한 바가 있나요?", ("네, 좋아요", "아니요, 괜찮아요"))
		if select_option_food == "네, 좋아요":
			food()
		elif select_option_food == "아니요, 괜찮아요":
			st.warning("END")
	
def food():
	global carbon_store_food
	food_persona = pd.read_csv('data/preprocessed/food/food_persona.csv')
	global carbon_food_category

	option_food_menu = st.multiselect('어떤 분류를 선택하시겠어요?', (food_persona.iloc[:,2].unique()))
	for _ in range(0, len(option_food_menu)):
		option_food_menu_df = food_persona.loc[food_persona.iloc[:,2] == option_food_menu[_]].reset_index()
		option_food_menu_persona = option_food_menu_df.iloc[:,4]
		option_food_menu_detail = option_food_menu_df.iloc[:,5]
		option_food_menu_co2= option_food_menu_df.iloc[:,8]
		option_food_menu_num =option_food_menu_df.iloc[:,7]

		st.write('{}! "{}"를 선택하셨습니다.'.format(option_food_menu_persona[0], option_food_menu))
		option_food_detail = st.multiselect('어떤 음식을 드실 예정인가요?', option_food_menu_detail[0].split(", "))
		st.write(option_food_menu_detail)

		# st.write('{}에서 발생한 탄소 배출량은 {}kgCO2입니다'.format(menu_detail, carbon_menu_element))
		# carbon_store_food = carbon_store_food + carbon_menu_element

	st.write("음식을 드시면서 배출하신 탄소량은 {}kgCO2 이에요".format(carbon_store_food))

	# select_option_store = st.radio("음식을 드실 계획인가요?", ("네, 먹을 거에요", "아니요, 아무것도 안 먹을 거에요"))
	# if select_option_store == "네, 먹을 거에요":
		# food_menu = pd.read_csv('data/preprocessed/food/food_menu.csv')

		# st.write(food_persona["페르소나"])
		# st.write(food_persona.iloc[:, 2])


		# option_food_persona = st.multiselect('어떤 음식을 드실 예정인가요?', (food_persona['페르소나'].unique()))
		# for _ in range(0, len(option_food_persona)):
		# 	food_persona_selected = food_persona.loc[food_persona['페르소나'] == option_food_persona[_]]
		# 	persona = (food_persona_selected)['페르소나']
		# 	# menu  = (food_persona.loc[food_persona['페르소나'] == option_food_persona[_]])['메뉴 종류']
		# 	menu = 0
		# 	menu_detail = (food_persona_selected)['세부 메뉴']
		# 	st.write(persona.name, menu,menu_detail)
		# 	st.write('{} : {}의 세부 메뉴는 {}입니다'.format(persona, menu, menu_detail))
		# 	carbon_menu_element = float((food_persona.loc[food_persona['페르소나'] == option_food_persona[_]])['평균탄소배출량'])
		
		
	# 	option_food_menu = st.multiselect('어떤 음식을 드실 예정인가요?', (food_persona.iloc[:,2].unique()))
	# 	for _ in range(0, len(option_food_menu)):
	# 		option_food_menu_df = food_persona.loc[food_persona.iloc[:,2] == option_food_menu[_]].reset_index()
	# 		option_food_menu_persona = option_food_menu_df.iloc[:,4]
	# 		option_food_menu_detail = option_food_menu_df.iloc[:,5]
	# 		option_food_menu_co2= option_food_menu_df.iloc[:,8]
	# 		option_food_menu_num =option_food_menu_df.iloc[:,7]
	# 		st.write(option_food_menu_persona[0])
	# 		x = option_food_menu_df.iloc[:,8]
	# 		st.write(option_food_menu_df)

	# 		# st.write('{}에서 발생한 탄소 배출량은 {}kgCO2입니다'.format(menu_detail, carbon_menu_element))
	# 		# carbon_store_food = carbon_store_food + carbon_menu_element

	# 	st.write("음식을 드시면서 배출하신 탄소량은 {}kgCO2 이에요".format(carbon_store_food))

	# elif select_option_store == "아니요, 아무것도 안 먹을 거에요":
	# 	st.success("배출하신 탄소량은 0kgCO2 이에요")

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
	st.title("[탄소 발자국 계산기] 음식")
	checkbox_store = st.checkbox("(Q1) 제주도에서 어떤 음식점에 가셨나요?")
	checkbox_food = st.checkbox("(Q2) 제주에서 어떤 음식을 드시고 싶은지 알려주세요")
	checkbox_ingredient = st.checkbox("(Q3) 제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")

	if checkbox_store:
		st.header("제주도에서 어떤 음식점에 가셨나요?")
		store()
	if checkbox_food:
		st.header("제주에서 어떤 음식을 드시고 싶은지 알려주세요")
		food()
	if checkbox_ingredient:
		st.header("제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")
		ingredient()

	# st.success('여행에서 나온 총 탄소 배출량은 {}kgCO2 입니다'.format(carbon_sum_co2+carbon_sum_traffic))
	# st.write('(Q1) 탄소 배출량은 ', carbon_sum_traffic, 'kgCO2 입니다')
	# st.write('(Q2) 탄소 배출량은 ', carbon_sum_co2, 'kgCO2 입니다')
	
if __name__ == '__main__':
	main()