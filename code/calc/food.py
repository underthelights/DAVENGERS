from os import write
import streamlit as st
import pandas as pd
import numpy as np

carbon_store_avg , carbon_store_food, carbon_food_category, carbon_food_igrd = 0,0,0,0
d = 0
def store():
	global carbon_store_avg, d
	# [TODO?] 제주시, 서귀포시 중 어디에 위치하나요? -> 네이버 구 주소 크롤링, 시/군까지?
	
	select_option_store = st.radio("이용하신 식당을 저희 데이터에서 찾아보시겠어요?", ("네, 찾아볼게요", "데이터베이스에 없어요"), key=d+417)

	if select_option_store == "네, 찾아볼게요":
		restaurant_carbon =pd.read_csv('data/preprocessed/food/restaurant_carbon.csv')
		
		option_res_name = st.multiselect('어디 식당에서 드실 계획인가요?', (restaurant_carbon['MCT_NM'].unique()), key=d+113)
		option_day = 0
		for _ in range(0, len(option_res_name)):
			carbon_store_element = float((restaurant_carbon.loc[restaurant_carbon['MCT_NM'] == option_res_name[_]])['carbon_avg'])
			st.write('{}에서 발생한 탄소 배출량은 {}kgCO2입니다'.format(option_res_name[_], round(carbon_store_element,2)))
			carbon_store_avg = carbon_store_avg + carbon_store_element

		st.success("식당에서 배출하신 총 탄소량은 {}kgCO2입니다".format(round(carbon_store_avg,2)))

	elif select_option_store == "데이터베이스에 없어요":
		st.warning("저희 데이터베이스에 있는 식당이 아닙니다")	
		select_option_food = st.radio("어떤 음식을 드실지 계획한 바가 있나요?", ("네, 있어요", "아니요, 없어요"))
		if select_option_food == "네, 있어요":
			food()
		elif select_option_food == "아니요, 없어요":
			st.warning("END")
	
def food():
	global carbon_store_food,d 
	food_persona = pd.read_csv('data/preprocessed/food/food_persona.csv')
	# st.write(food_persona)
	global carbon_food_category

	option_food_menu = st.multiselect('어떤 분류를 선택하시겠어요?', (food_persona.iloc[:,2].unique()), key=d+813)
	for _ in range(0, len(option_food_menu)):
		option_food_menu_df = food_persona.loc[food_persona.iloc[:,2] == option_food_menu[_]].reset_index()
		option_food_menu_persona = option_food_menu_df.iloc[:,4]
		option_food_menu_detail = option_food_menu_df.iloc[:,5]
		option_food_menu_co2= option_food_menu_df.iloc[:,8]
		option_food_menu_num =option_food_menu_df.iloc[:,7]

		st.write('{}! "{}"를 선택하셨습니다'.format(option_food_menu_persona[0], option_food_menu[0]))
		option_food_detail = st.multiselect('어떤 음식을 드실 예정인가요?', option_food_menu_detail[0].split(", "))
		# st.write(option_food_menu_detail)

		carbon_store_food += option_food_menu_co2
		# st.write(carbon_store_food)
		st.success("음식을 드시면서 배출하신 탄소 배출량은 {}kgCO2 이에요".format(round(carbon_store_food[0],2)))


def ingredient():
	global carbon_food_igrd,d
	select_option_store = st.radio("음식을 드셨나요", ("네, 먹었어요", "아니요, 아무것도 안 먹었어요"), key=d+1113)
	if select_option_store == "네, 먹었어요":
		igrd = pd.read_csv('data/preprocessed/food/food_revised.csv')
		option_food_type = st.multiselect('드신 음식의 분류를 알려주세요.', (igrd['type_detail'].unique()))
		#[TODO] 한국어로 reindex화 진행
		for _ in range(0, len(option_food_type)):
			carbon_food_df = pd.DataFrame(igrd.loc[igrd['type_detail'] == option_food_type[_]])['CO2']
			# st.write(carbon_food_df.unique()[0])
			carbon_food_igrd += carbon_food_df.unique()[0]
		st.success("음식을 드시면서 배출하신 탄소 배출량은 {}kgCO2 이에요".format(round(carbon_food_igrd,2)))

	elif select_option_store == "아니요, 아무것도 안 먹었어요":
		st.success("배출하신 탄소 배출량은 0kgCO2 이에요")


def main():
	global d, carbon_store_avg , carbon_store_food, carbon_food_category, carbon_food_igrd
	st.title("[탄소 발자국 계산기] 음식")
	checkbox_store = st.checkbox("(Q1) 제주도에서 어떤 음식점에 가셨나요?")
	checkbox_food = st.checkbox("(Q2) 제주에서 어떤 음식을 드시고 싶은지 알려주세요")
	checkbox_ingredient = st.checkbox("(Q3) 제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")
	if (checkbox_store & checkbox_food) :
		st.warning("하나의 질문만 선택해주세요!")
		pass
	elif checkbox_store:
		st.header("제주도에서 어떤 음식점에 가셨나요?")
		store()
	elif checkbox_food:
		st.header("제주에서 어떤 음식을 드시고 싶은지 알려주세요")
		food()
	
	elif checkbox_ingredient:
		st.header("제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")
		ingredient()
	carbon_store_avg , carbon_store_food, carbon_food_category, carbon_food_igrd = 0,0,0,0
	d = 0

	
if __name__ == '__main__':
	main()