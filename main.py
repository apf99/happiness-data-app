import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('happy.csv')

st.title('In Search of Happiness')
x = st.selectbox('Select the data for the X-axis',
                 ('GDP', 'Happiness', 'Generosity'))
y = st.selectbox('Select the data for the Y-axis',
                 ('GDP', 'Happiness', 'Generosity'))
st.subheader(f'{x} and {y}')

labels = {'x': x, 'y': y}
figure = px.scatter(x=df[x.lower()], y=df[y.lower()], labels=labels)
st.plotly_chart(figure)
