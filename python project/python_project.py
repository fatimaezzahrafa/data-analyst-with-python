import streamlit as st
import pandas as pd 
import numpy as py
from matplotlib import pyplot as plt


st.title("Data Analysis with Python")

uploaded_file = st.file_uploader("covid_worldwide(1).csv")
if uploaded_file:
    st.markdown('----')
df = pd.read_csv('C:/Users/hp/Desktop/python project/covid_worldwide (1).csv')
st.dataframe(df)  # Load the data
#
#checking the structure and summary
st.write(df.head())  # Display the first 5 rows of the DataFrame
st.write(df.tail())  # Display the last 5 rows of the DataFrame
st.write(df.info())  # Display information about the DataFrame (column names, data types, etc.)
st.write(df.describe()) #Display summary statistics of the DataFrame (count, mean, std, min, max, etc.)
st.write(df=df.interpolate(method='linear'))# Fill missing values using linear interpolation and display the resulting DataFrame
st.write(df.count()) # Display the number of non-null values in each column of the DataFrame
st.write(df.isnull().sum()) # Display the number of missing values in each column of the DataFrame









