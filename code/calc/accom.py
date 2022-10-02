from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd
import numpy as np

accom_total = pd.read_csv('data/preprocessed/accom/accom_total.csv')
accom  = pd.read_csv('data/preprocessed/accom/accom.csv')

st.title("[탄소 발자국 계산기] 숙소")
carbon_accom, carbon_accom_total = 0, 0
def q1():
	global carbon_accom
	st.header("머무시는 숙소의 이름과 숙박일수를 알려주세요")

	option_accom_name = st.multiselect('어디 숙소에 묵으셨나요?', (accom['name'].unique()))
	# option_day = []
	# for _ in range(0,len(option_accom_name)):
	# 	option_day.append(None)
	# st.write(option_day, len(option_day))
	option_day = 0
	for _ in range(0, len(option_accom_name)):
		carbon_accom_element = float((accom.loc[accom['name'] == option_accom_name[_]])['carbon'])
		option_day = st.number_input('얼마나 {}에 머무르셨나요?'.format(option_accom_name[_]), min_value=1, step = 1)
		# st.write('총 {}일 해당 숙소에서 지내셨습니다'.format(option_day))
		st.write('{}에 머무르며 발생된 탄소 배출량은 {}kgCO2입니다'.format(option_accom_name[_], carbon_accom_element*option_day))
		carbon_accom = carbon_accom + carbon_accom_element*option_day

	st.write('숙소의 총 탄소 배출량 합계는 {}kgCO2입니다'.format(carbon_accom))

def q2():
	global carbon_accom_total
	st.header("머무시는 숙소의 형태와 숙박일수를 알려주세요")
	option_accom_type = st.multiselect("숙소의 형태가 어떠셨나요", (accom_total['type'].unique()))
	
	option_day = 0
	for _ in range(0, len(option_accom_type)):
		carbon_accom_element = float((accom_total.loc[accom_total['type'] == option_accom_type[_]])['carbon'])
		option_day = st.number_input('얼마나 {}에 머무르셨나요?'.format(option_accom_type[_]), min_value=1, step = 1)
		# st.write('총 {}일 해당 숙소에서 지내셨습니다'.format(option_day))
		if(carbon_accom_element!=0): 
			st.write('{}에 머무르며 발생된 탄소 배출량은 {}kgCO2입니다'.format(option_accom_type[_], carbon_accom_element*option_day))
		else : 
			st.write('{}에서의 탄소 배출량은 측정할 수 없으니 0으로 대체합니다'.format(option_accom_type[_]))
		carbon_accom_total = carbon_accom_total + carbon_accom_element*option_day

	st.write('총 탄소 배출량 합계는 {}kgCO2입니다'.format(carbon_accom_total))


def main():
	q1()
	q2()
	
if __name__ == '__main__':
	main()
