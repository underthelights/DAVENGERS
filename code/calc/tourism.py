from os import write
from click import option
import streamlit as st
import pandas as pd
import numpy as np


d = 0
co2_nature, co2_theme, co2_perf, co2_leisure = 0, 0, 0, 0

def ref():
	st.header("Reference.")
	if st.button("참고논문1"):
		st.write('[제주 생태관광 과정의 탄소 배출량 추정(한국기후변화학회지), 이원아 et al., 2019](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE08746881)')
	if st.button("참고논문2"):
		st.write('[Carbon Footprint Evaluation Based on Tourist Consumption toward Sustainable Tourism in Japan, Yusuke Kitamura et al., 2020](https://www.mdpi.com/2071-1050/12/6/2219/htm)')

def nature():
	global co2_nature, d

	tour_nature_co2 = pd.read_csv('data/preprocessed/tour/tour_nature_co2.csv')
	option_tour_nature = st.multiselect('🌳 자연 관광지에서 어떤 활동을 하셨나요? (복수 선택 가능)', tour_nature_co2['활동'], key = d+317)


	for _ in range(0, len(option_tour_nature)):
		co2_nature = co2_nature + float((tour_nature_co2.loc[tour_nature_co2['활동'] == option_tour_nature[_]])['1인당 탄소배출량'])

	st.write('자연 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_nature,2)))
	

def theme():
	global co2_theme, d
	val0, val1, val2 = 6518, 676712, 0
	option_tour_theme = st.radio("주중 혹은 주말 중 언제 테마파크에 방문하셨나요?", ("주중", "주말"), key = d+417)

	if option_tour_theme == "주중":
		val2 = 0.54
	else:
		val2 = 0.46
	
	co2_theme = (val1)/(val0 * val2)
	st.write('테마파크에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_theme,2)))

def perf():
	global co2_perf, d
	val0, val1, val2 = 3346, 0, 0
	option_tour_perf = st.radio("공연전시에서 어떤 활동을 하셨나요?", ("박물관/전시 관람", "스포츠 관람"), key = d+529)

	if option_tour_perf == "박물관/전시 관람":
		val1 = 295890
	else:
		val1 = 676712

	option_tour_perf_day = st.radio("주중 혹은 주말 중 언제 테마파크에 방문하셨나요?", ("주중", "주말"), key = d+719)

	if option_tour_perf_day == "주중":
		val2 = 0.54
	else:
		val2 = 0.46
	
	co2_perf = (val1)/(val0 * val2)
	st.write('테마파크에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_perf,2)))

def leisure():
	global co2_leisure, d
	tour_leisure_co2 = pd.read_csv('data/preprocessed/tour/tour_leisure_co2.csv')
	
	val0, val1 = 859, 293150
	val2, val3 = 0, 0
	option_tour_ls = st.multiselect('레저/체험 관광지에서 어떤 활동을 하셨나요? (복수 선택 가능)', tour_leisure_co2['활동'], key=d+1013)

	for _ in range(0, len(option_tour_ls)):
		val2 = val2 + float((tour_leisure_co2.loc[tour_leisure_co2['활동'] == option_tour_ls[_]])['1인당 탄소배출량'])

	option_tour_perf_day = st.radio("주중 혹은 주말 중 언제 테마파크에 방문하셨나요?", ("주중", "주말"), key = d+1019)

	if option_tour_perf_day == "주중":
		val3 = 0.54
	else:
		val3 = 0.46
	
	co2_leisure = ((val1)/(val0 * val3))+(val2)
	
	st.write('레저/체험 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_leisure,2)))

def q():
	global d
	st.header("제주도에서 어떤 관광지에 방문하셨나요?")
	option_visit = st.radio("자연, 테마파크, 공연전시, 레저/체험 중 하나만 선택해주세요", ('자연','테마파크','공연전시','레저/체험'),key=d+37)
	if option_visit == '자연':
		st.write(':deciduous_tree: {}를 선택하셨습니다'.format(option_visit))
		nature()
	elif option_visit == '테마파크':
		st.write(':national_park: {}를 선택하셨습니다'.format(option_visit))
		theme()
	elif option_visit == '공연전시':
		st.write(':art: {}를 선택하셨습니다'.format(option_visit))
		perf()
	elif option_visit == '레저/체험':
		st.write(':woman-surfing: {}를 선택하셨습니다'.format(option_visit))
		leisure()
	

def days(option_days):
	global d
	q()

def main():
	global d
	st.title("[탄소 발자국 계산기] 관광")
	
	option_days = st.number_input('관광지를 몇 개 방문하셨나요?', min_value=1, max_value=20, step=1)
	# st.write('The current number is ', option_days)	
	if option_days == 1:
		days(option_days)
	
	for _ in range(2,20, 1):
		if option_days == _:
			for _ in range(0, option_days):
				st.warning('{}번째 관광지'.format(_+1))
				d = d+1
				days(_)
	ref()
if __name__ == '__main__':
	main()