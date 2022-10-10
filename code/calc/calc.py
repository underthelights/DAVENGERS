from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd


st.title("탄소 발자국 👣 계산기")
option_calc_type = st.multiselect('어떤 탄소 계산기를 이용하실 건가요?', ("교통", "음식", "관광", "숙소"))

for _ in range(0, len(option_calc_type)):
    
    import food, tourism, traffic, accom
    if(option_calc_type[_] == "교통"):
        st.info(':oncoming_automobile: 교통 탄소계산기를 이용할게요')
        traffic.main()
    if(option_calc_type[_] == "음식"):
        st.info(':stuffed_flatbread: 음식 탄소계산기를 이용할게요')
        food.main()
    if(option_calc_type[_] == "관광"):
        st.info(':camping: 관광 탄소계산기를 이용할게요')
        tourism.main()
    if(option_calc_type[_] == "숙소"):
        st.info(':hotel: 숙소 탄소계산기를 이용할게요')
        accom.main()