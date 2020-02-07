import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly_express as px

'''
# Team and Nationality App

This is my first look on Streamlit. This app allows you to choose and visualize players
from certain clubs and nationalities

'''

df = st.cache(pd.read_csv)('nhl_players.csv')

teams = st.sidebar.multiselect('Show Player for clubs? (abbreviation)', df['Team'].unique())

nationalities = st.sidebar.multiselect('Show Players from Nationalities?',
df['Cntry'].unique())

# Filter dataframe 
new_df = df[(df['Team'].isin(teams)) &
(df['Cntry'].isin(nationalities))]

# Write dataframe to screen
cols = ['Last Name', 'First Name', 'Cntry', 'Position', 'GP', 'G', 'A', 'PTS', 'Salary','Cap Hit']
if st.checkbox('Show dataframe', value=True):
    st.write(new_df[cols])
# st.write(new_df[cols])

# Create figure using plotly express
# options = st.sidebar.multiselect('Select columns', new_df.columns)
x = st.sidebar.selectbox('Choose variable in X-axis', cols, index=9)
# cols = [i for i in cols if i != x]
# x = options[0]
y = st.sidebar.selectbox('Choose variable in Y-axis', cols, index=7)
# y = options[1]
color = st.sidebar.selectbox('Choose variable in Color-axis', cols, index=2)
# color = options[2]
if teams and nationalities and x and y and color:
    fig = px.scatter(new_df, x=x, y=y, color=color, hover_name='Last Name')

    # Plot it
    st.plotly_chart(fig)

