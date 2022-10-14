from os import write
import streamlit as st
import pandas as pd
import numpy as np

# [TODO] day별 탄소 배출량, 총합 탄소 배출량 -> global 
# 		n번째 밤의 탄소 배출량은~	
# 		모든 밤의 탄소 배출량은~
accom_total = pd.read_csv('data/preprocessed/accom/accom_total.csv')
accom  = pd.read_csv('data/preprocessed/accom/accom.csv')

carbon_accom1, carbon_accom_total, carbon_accom2 = 0, 0, 0

d = 0
def q1():
	global carbon_accom1, carbon_accom_total, d
	st.header("🏨머무시는 숙소의 이름과 숙박일수를 알려주세요")
	
	option_accom_name = st.multiselect('어디 숙소에 묵으셨나요?', (accom['name'].unique()), key=d+37)
	# option_day = []
	# for _ in range(0,len(option_accom_name)):
	# 	option_day.append(None)
	# st.write(option_day, len(option_day))
	option_day = 0
	for _ in range(0, len(option_accom_name)):
		carbon_accom_element = float((accom.loc[accom['name'] == option_accom_name[_]])['carbon'])
		option_day = st.number_input('얼마나 {}에 머무르셨나요?'.format(option_accom_name[_]), min_value=1, step = 1)
		# st.write('총 {}일 해당 숙소에서 지내셨습니다'.format(option_day))
		st.write('{}에 머무르며 발생된 탄소 배출량은 {}kgCO2입니다'.format(option_accom_name[_], round(carbon_accom_element*option_day,2)))
		carbon_accom1 = carbon_accom1 + carbon_accom_element*option_day

	st.info('숙소의 총 탄소 배출량 합계는 {}kgCO2입니다'.format(round(carbon_accom1,2)))

def q2():
	global carbon_accom_total, carbon_accom2, d
	st.header("머무시는 숙소의 형태와 숙박일수를 알려주세요")
	st.write(d)
	option_accom_type = st.multiselect("숙소의 형태가 어떠셨나요", (accom_total['type'].unique()), key=d+1)
	
	option_day = 0
	for _ in range(0, len(option_accom_type)):
		carbon_accom_element = float((accom_total.loc[accom_total['type'] == option_accom_type[_]])['carbon'])
		option_day = st.number_input('얼마나 {}에 머무르셨나요?'.format(option_accom_type[_]), min_value=1, step = 1)
		# st.write('총 {}일 해당 숙소에서 지내셨습니다'.format(option_day))
		if(carbon_accom_element!=0): 
			st.write('{}에 머무르며 발생된 탄소 배출량은 {}kgCO2입니다'.format(option_accom_type[_], round(carbon_accom_element*option_day,2)))
		else : 
			st.write('{}에서의 탄소 배출량은 측정할 수 없으니 0으로 대체합니다'.format(option_accom_type[_]))
		carbon_accom_total = carbon_accom_total + carbon_accom_element*option_day

	st.info('총 탄소 배출량 합계는 {}kgCO2입니다'.format(round(carbon_accom_total,2)))

def days(option_days):
	global d
	q1()
	select_option_accom_day1 = st.radio("이용하신 숙소가 저희 데이터에 없습니까?", ("아니요, 있습니다", "네, 없습니다"), key=d+13)
	if select_option_accom_day1 == "아니요, 있습니다":
		pass
	else :
		q2()


def main():
	global carbon_accom1, carbon_accom_total, carbon_accom2
	st.title("[탄소 발자국 계산기] 숙소")
	global d
	option_days = st.number_input('숙소에서 몇 박 묵으셨나요?', min_value=1, max_value=3, step=1)
	# st.write('The current number is ', option_days)	
	if option_days == 1:
		days(option_days)
	
	elif option_days == 2:
		for _ in range(0, option_days):
			st.warning('🌙 {}번째 밤'.format(_+1))
			d = d+1
			days(_)
	
	elif option_days == 3:
		for _ in range(0, option_days):
			st.warning('🌙 {}번째 밤'.format(_+1))
			d = d+1
			days(_)
	carbon_accom1, carbon_accom_total, carbon_accom2 = 0, 0, 0
if __name__ == '__main__':
	main()
