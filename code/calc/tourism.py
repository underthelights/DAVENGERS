from os import write
from click import option
import streamlit as st
import pandas as pd
import numpy as np

d = 0
co2_nature, co2_theme, co2_perf, co2_leisure = 0, 0, 0, 0
co2_sum = 0

def ref():
	st.header("Reference.")
	if st.button("참고논문1"):
		st.write('[제주 생태관광 과정의 탄소 배출량 추정(한국기후변화학회지), 이원아 et al., 2019](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE08746881)')
	if st.button("참고논문2"):
		st.write('[Carbon Footprint Evaluation Based on Tourist Consumption toward Sustainable Tourism in Japan, Yusuke Kitamura et al., 2020](https://www.mdpi.com/2071-1050/12/6/2219/htm)')

def nature():
	global co2_nature, d
	option_tour_nature = st.multiselect('🌳 자연 관광지에서 어떤 활동을 하셨나요? (복수 선택 가능)', ['산', '바다'], key = d+917)
	st.info('성산일출봉과 같은 관광지는 산, 후포해변과 같은 관광지는 바다에 해당합니다.')
	val1=0
	if option_tour_nature == "산":
		val1 = 0.000950
	else:
		val1 = 0.000950

	for _ in range(0, len(option_tour_nature)):
		co2_nature = co2_nature + val1

	# st.write('자연 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_nature,2)))
	st.write('자연 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(co2_nature)) #round(co2_nature,2)
	#[TODO] 2의 자리에서 반올림하여 0이 나옴.
	

def theme():

	global co2_theme, d
	option_tour_theme = st.multiselect('🌳 테마파크/테마관광지에서 어떤 활동을 하셨나요? (복수 선택 가능)', ['문화유적지', '문화유적지 외'], key = d+191)
	st.info('문화유적지 외의 테마파크/테마관광지는 윈트1947 카트 테마파크, 제주무민랜드 등이 해당합니다')
	val1=0
	if option_tour_theme == "문화유적지":
		val1 = 0.024836
	else:
		val1 = 0.024836

	for _ in range(0, len(option_tour_theme)):
		co2_theme = co2_theme + val1

	# st.write('자연 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(round(co2_nature,2)))
	st.write('테마파크에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(co2_theme))
	
def perf():
	global co2_perf, d
	option_tour_perf = st.radio('🌳 공연이나 전시에 가신 적 있나요?', ['예', '아니오'], key = d+1779)
	val = 0

	if option_tour_perf == "예":
		val1 = 0.024836
	else:
		val1 = 0

	co2_perf = co2_perf + val1
	st.write('공연/전시 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(co2_perf))

def leisure():
	global co2_leisure, d
	option_tour_lei = st.multiselect('🌳 레저/체험 관광지에서 어떤 활동을 하셨나요? (복수 선택 가능)', ['골프', '공방', '드라이브', '승마','유람선/잠수함', '전망대', '체험농장', '캠핑', '해양레저', '헬스케어'], key = d+311)
	st.info('해안도로는 드라이브, 제주어울림감귤체험농장은 체험농장 분류로 선택해주시면 됩니다.')
	val1=0.106358
	for _ in range(0, len(option_tour_lei)):
		co2_leisure = co2_leisure + val1

	st.write('레저/체험 관광지에서 배출하신 탄소 배출량은 {}kgCO2입니다.'.format(co2_leisure))


def q():
	global d, co2_sum, co2_nature, co2_theme, co2_perf, co2_leisure
	st.header("제주도에서 어떤 관광지에 방문하셨나요?")
	st.header(':deciduous_tree: 자연 관광지')
	nature()
	st.header(':national_park: 테마파크/테마관광지')
	theme()
	st.header(':art: 공연/전시')
	perf()
	st.header(':woman-surfing: 레저/체험')
	leisure()
	co2_sum += co2_nature+ co2_theme+ co2_perf+ co2_leisure
	st.header('관광지에서 배출하신 총 탄소배출량은 {}kgCO2입니다'.format(round(co2_sum,2)))

def days():
	global d
	q()

def main():
	global d
	global d, co2_sum, co2_nature, co2_theme, co2_perf, co2_leisure
	st.title("[탄소 발자국 계산기] 관광")
	
	days()
	# option_days = st.number_input('관광지를 몇 개 방문하셨나요?', min_value=1, max_value=20, step=1)
	# # st.write('The current number is ', option_days)	
	# if option_days == 1:
	# 	days(option_days)
	
	# for _ in range(2,20, 1):
	# 	if option_days == _:
	# 		for _ in range(0, option_days):
	# 			st.warning('{}번째 관광지'.format(_+1))
	# 			d = d+1
	# 			days(_)
	co2_sum, co2_nature, co2_theme, co2_perf, co2_leisure = 0, 0,0,0,0
	ref()


if __name__ == '__main__':
	main()