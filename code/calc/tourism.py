from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd

st.title("[탄소 발자국 계산기] 관광")

def main():
	# checkbox_store = st.checkbox("(Q1) 제주도에서 어떤 음식점에 가셨나요?")
	# checkbox_food = st.checkbox("(Q2) 제주도에서 어떤 음식을 드셨나요?")
	# checkbox_ingredient = st.checkbox("(Q3) 제주도에서 드신 음식이 어떤 재료로 이루어져 있나요?")

	# if checkbox_store:
	# 	store()
	# if checkbox_food:
	# 	food()
	# if checkbox_ingredient:
	# 	ingredient()
	pass
	# st.success('여행에서 나온 총 탄소 배출량은 {}kgCO2 입니다'.format(carbon_sum_co2+carbon_sum_traffic))
	# st.write('(Q1) 탄소 배출량은 ', carbon_sum_traffic, 'kgCO2 입니다')
	# st.write('(Q2) 탄소 배출량은 ', carbon_sum_co2, 'kgCO2 입니다')
	
if __name__ == '__main__':
	main()