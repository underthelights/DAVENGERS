from os import write
from tabnanny import check
from click import option
import streamlit as st
import pandas as pd
import numpy as np


st.title("[탄소 발자국 계산기] 숙소")
def t1():
	t1 = pd.read_csv('data/rename/t1_JEJU_MERCHANT.csv')
	st.write(t1)

def main():
	t1()
	
if __name__ == '__main__':
	main()

	df = pd.DataFrame(
		np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
		columns=['lat', 'lon'])

	st.map(df)