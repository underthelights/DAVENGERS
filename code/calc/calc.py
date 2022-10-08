from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd


st.title("탄소 발자국 계산기")

# option_calc = st.radio("계산기를 사용하시겠어요?", ("네, 사용할게요", "아니요, 사용하지 않을게요"))
# if option_calc == "네, 사용할게요":
#     option_calc_type = st.multiselect('어떤 탄소 계산기를 이용하실 건가요?', ("교통", "음식", "관광", "숙소"))

#     for _ in range(0, len(option_calc_type)):
#         st.write(option_calc_type[_],'의 탄소계산기를 이용할게요')
#         if(option_calc_type[_] == "교통"):
#             traffic.main()
#         if(option_calc_type[_] == "음식"):
#             food.main()
#         if(option_calc_type[_] == "관광"):
#             tourism.main()
#         if(option_calc_type[_] == "숙소"):
#             accom.main()

# elif option_calc == "아니요, 사용하지 않을게요":
#     pass
option_calc_type = st.multiselect('어떤 탄소 계산기를 이용하실 건가요?', ("교통", "음식", "관광", "숙소"))

for _ in range(0, len(option_calc_type)):
    st.write(option_calc_type[_],'의 탄소계산기를 이용할게요')
    import food, tourism, traffic, accom
    if(option_calc_type[_] == "교통"):
        traffic.main()
    if(option_calc_type[_] == "음식"):
        food.main()
    if(option_calc_type[_] == "관광"):
        tourism.main()
    if(option_calc_type[_] == "숙소"):
        accom.main()