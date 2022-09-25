from os import write
from tabnanny import check
import streamlit as st
import pandas as pd

st.title("[탄소 발자국 계산기] 교통수단")


# df = pd.read_csv('web/carbon/data/traffic.csv')
# if st.button('데이터 보기'):
# 	st.dataframe(df)

if st.button('Reference'):
    st.write('Google Flight', 'https://www.google.com/travel/flights/')


carbon_sum_traffic, carbon_sum_plane, carbon_sum_ship, carbon_sum_car = 0, 0, 0, 0
carbon_sum_co2, carbon_sum_self, carbon_sum_rent, carbon_sum_public = 0, 0, 0, 0

def plane():
	global carbon_sum_traffic, carbon_sum_plane
	st.header("비행기를 선택하셨습니다")

	airport = ['김포공항(GMP)', '김해공항(PUS)']
	seat_type = ['이코노미 (Economy)', '비즈니스 (Business)']
	carbon = [56, 77, 41, 61]


	st.write('출발했던 공항을 선택해주세요')	
	air_start = st.selectbox('다른 공항을 탑승하셨다면, 김포공항(GMP)와 김해공항(PUS) 중 더 가까운 공항을 선택해주세요', (airport))
	
	st.write('어떤 좌석에 앉으셨나요?')	
	air_seat = st.selectbox('비즈니스, 이코노미 중에 선택해주세요', (seat_type))

	if (air_start == airport[0]): #GMP
		st.write(airport[0], '에서 비행기를 타고')
		if (air_seat == seat_type[0]):#econ
			st.write('제주로 이동하는 비행기를 타는 데 배출한 탄소량은', carbon[0]*2, '이에요')
			carbon_sum_plane = carbon_sum_plane + carbon[0]
		elif (air_seat == seat_type[1]):#bus
			st.write('제주로 이동하는 비행기를 타는 데 배출한 탄소량은', carbon[1]*2, '이에요')
			carbon_sum_plane += carbon[1]

	if (air_start == airport[1]): #PUS
		st.write(airport[1], '에서 비행기를 타고')
		if (air_seat == seat_type[0]):
			st.write('제주로 이동하는 비행기를 타는 데 배출한 탄소량은', carbon[2]*2, '이에요')
			carbon_sum_plane += carbon[2]
		elif (air_seat == seat_type[1]):
			st.write('제주로 이동하는 비행기를 타는 데 배출한 탄소량은', carbon[3]*2, '이에요')
			carbon_sum_plane += carbon[3]
	# ⇒ 김포/이코노미: 56kg, 김해/이코노미: 41kg, 김포/비즈니스: 77kg, 김해/비즈니스: 61kg

	carbon_sum_traffic += carbon_sum_plane

def ship():
	global carbon_sum, carbon_sum_ship
	st.header("배를 선택하셨습니다")

def car():
	global carbon_sum, carbon_sum_car
	st.header("자동차를 선택하셨습니다")


def traffic():
	global carbon_sum_traffic, carbon_sum_plane, carbon_sum_ship, carbon_sum_car
	st.header("제주도까지 어떻게 이동하셨나요?")
	# 귀하가 여행 시 이용했던 교통수단을 체크해 주세요.
	checkbox_plane = st.checkbox('비행기 (항공편)', value=True)
	checkbox_ship = st.checkbox('배')
	checkbox_car = st.checkbox('자동차')
	

	if checkbox_plane:
		st.write('비행기를 선택하셨습니다.')
		plane()
	if checkbox_ship:
		st.write('배를 선택하셨습니다.')
		ship()
	if checkbox_car:
		st.write('자동차를 선택하셨습니다.')
		car()


	# if checkbox_plane==True:
	# 	plane()
	# if checkbox_ship==True:
	# 	ship()
	# if checkbox_car==True:
	# 	car()

	carbon_sum_traffic = carbon_sum_plane + carbon_sum_ship + carbon_sum_car
	
	st.header('총 탄소배출량은 {}입니다'.format(carbon_sum_traffic*2))
	st.write('그 중 비행기로 배출한 탄소 배출량은 ', carbon_sum_plane*2, '입니다')
	st.write('그 중 배로 배출한 탄소 배출량은 ', carbon_sum_ship*2, '입니다')
	st.write('그 중 자동차로 배출한 탄소 배출량은 ', carbon_sum_car*2, '입니다')

def self_car():
	global carbon_sum_self
	
	car_man = st.slider('함께 탑승한 인원수를 입력해주세요', 1, 8)
	st.text('함께 {}명 탑승했습니다 '.format(car_man))

	car_distance_st = st.slider('집에서 출발 항구까지의 이동 거리를 알려주세요', 0, 1000)/car_man
	st.text('자동차로 집에서 출발 항구까지 이동한 총 이동거리는 {}km입니다 (화물차로 수송) '.format(car_distance_st))
	car_distance_ar = st.slider('출발 항구까지에서 제주항까지의 이동 거리를 알려주세요', 0, 1000)/car_man
	st.text('자동차로 집에서 출발 항구까지에서 제주항까지 이동한 총 이동거리는 {}km입니다 (해운으로 수송) '.format(car_distance_ar))
	carbon_car_dis_st, carbon_car_dis_ar = car_distance_st *474.9 / 1000 * 1.5*2, car_distance_ar *474.9 / 1000 * 1.5*2

	carbon_sum_self = carbon_car_dis_ar + carbon_car_dis_st
	
	car = pd.read_csv('data/preprocessed/car.csv', encoding='cp949')
	option_brand = st.selectbox('브랜드 선택', (car['BRAND'].unique()))
	car_detail = car.loc[(car['BRAND'] == option_brand)]
	option_car = st.selectbox('상세 차종 선택', (car_detail['MODEL'].unique()))
	# car_distance_st = st.slider('집에서 출발 항구까지의 이동 거리를 알려주세요', 0, 1000)/car_man
	car_factor = car.loc[(car['MODEL'] == option_car)]['FACTOR']
	st.write(car_factor)
	st.write('자동차 이용으로 배출한 탄소량은 {}kgCO2입니다'.format(car_factor * car_distance_st))


	st.header('차를 제주도로 이동시키기 위해 배출한 탄소배출량은 {}입니다'.format(carbon_car_dis_st+carbon_car_dis_ar))
	st.write('화물차로 이동시키기 위해 배출한 탄소량은 ', carbon_car_dis_st, 'kgCO2입니다')
	st.write('해운으로 이동시키기 위해 배출한 탄소량은 ', carbon_car_dis_ar, 'kgCO2입니다')
	st.write('(차량 평균 무게 1.5t 가정)')
	# st.write(option_car)



def rent_car():
	# 버스로 이동한 거리를 알려주세요!
	st.write("렌터카로 이동한 거리를 알려주세요!")
	rent_distance = st.slider('애월에서 한림까지의 거리는 00km에요', 0, 1000, key='bus')
	st.write('버스로 총 ', rent_distance, 'km 이동하셨습니다')

	carbon_sum_rent = rent_distance
	carbon_avg_rent = 0
	st.header("렌터카으로 배출한 총 탄소량은 {}입니다".format(carbon_sum_rent))
	if carbon_avg_rent > carbon_sum_rent:
		st.write("제주 렌터카 TOP20의 평균 탄소배출량에 비해 {}kgCO2만큼 적어요".format(carbon_avg_rent - carbon_sum_rent))
	elif carbon_avg_rent <= carbon_sum_rent:
		st.write("제주 렌터카 TOP20의 평균 탄소배출량에 비해 {}kgCO2만큼 많아요".format(-carbon_avg_rent + carbon_sum_rent))
	
	st.write("추가 꿀팁! 자전거의 탄소 배출량은 0이에요~")

def public():
	global carbon_sum_public
	# 버스로 이동한 거리를 알려주세요!
	st.write("버스로 이동한 거리를 알려주세요!")
	bus_distance = st.slider('애월에서 한림까지의 거리는 00km에요', 0, 1000, key='bus')
	st.write('버스로 총 ', bus_distance, 'km 이동하셨습니다')

	# 지하철로 이동한 거리를 알려주세요!**
	st.write("지하철로 이동한 거리를 알려주세요!")
	subway_distance = st.slider('애월에서 한림까지의 거리는 00km에요', 0, 1000, key='subway')
	st.write('지하철로 총 ', subway_distance, 'km 이동하셨습니다')

	carbon_sum_public = carbon_sum_public + bus_distance*27.7/1000 + subway_distance*1.53/1000
	st.header("대중교통으로 배출한 총 탄소량은 {}입니다".format(carbon_sum_public))
	st.write("그 중 버스 이용으로 배출한 탄소량은 {}이며, 지하철 이용으로 배출한 탄소량은 {}kgCO2입니다".format(bus_distance*27.7/1000, subway_distance*1.53/1000))
	st.write("추가 꿀팁! 자전거의 탄소 배출량은 0이에요~")

def co2():
	global carbon_sum_co2, carbon_sum_self, carbon_sum_rent, carbon_sum_public
	st.header("여행 시 이용한 교통수단 별 탄소배출량을 적어주세요")
	st.write("Q1에서 1번 또는 2번을 선택했을 시 해당 공항/항구로 이동하는데 이용한 교통수단도 포함시켜주세요~")
	checkbox_selfcar = st.checkbox('자차')
	checkbox_rentcar = st.checkbox('렌터카')
	checkbox_public = st.checkbox('대중교통')
	

	if checkbox_selfcar:
		st.write('자차를 타고 이동하셨습니다')
		self_car()
	if checkbox_rentcar:
		st.write('렌터차를 타고 이동하셨습니다')
		rent_car()
	if checkbox_public:
		st.write('대중교통을 타고 이동하셨습니다')
		public()

	carbon_sum_co2 = carbon_sum_self + carbon_sum_rent + carbon_sum_public
	
	st.header('(Q2)에서의 총 탄소배출량은 {}kgCO2입니다'.format(carbon_sum_co2))
	if checkbox_selfcar:
		st.write('자차로 배출한 탄소 배출량은 ', carbon_sum_self, '입니다')
	if checkbox_rentcar:
		st.write('렌터카로 배출한 탄소 배출량은 ', carbon_sum_rent, '입니다')
	if checkbox_public:
		st.write('대중교통으로 배출한 탄소 배출량은 ', carbon_sum_public, '입니다')

def main():
	global carbon_sum_co2, carbon_sum_traffic
	checkbox_traffic = st.checkbox("(Q1) 제주도까지 어떻게 이동하셨나요?")
	checkbox_co2 = st.checkbox("(Q2) 여행 시 이용한 교통수단 별 탄소배출량을 적어주세요")

	if checkbox_traffic:
		traffic()
	if checkbox_co2:
		co2()
	st.success('여행에서 나온 총 탄소 배출량은 {}kgCO2 입니다'.format(carbon_sum_co2+carbon_sum_traffic))
	st.write('(Q1) 탄소 배출량은 ', carbon_sum_traffic, 'kgCO2 입니다')
	st.write('(Q2) 탄소 배출량은 ', carbon_sum_co2, 'kgCO2 입니다')
	
if __name__ == '__main__':
	main()