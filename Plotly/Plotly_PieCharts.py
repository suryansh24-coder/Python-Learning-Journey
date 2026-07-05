import pandas as pd 
import plotly.express as px

df = pd.read_csv('social_media_engagement.csv')

Grouped_data = df.groupby(by='platform')['likes'].sum().reset_index()
fig = px.pie(data_frame=Grouped_data , names='platform' , values='likes' , color_discrete_sequence=px.colors.qualitative.Bold_r)
fig.show()

fig = px.pie(data_frame=Grouped_data , names='platform' , values='likes' , hole=0.4 , color_discrete_sequence=px.colors.qualitative.Bold_r)
fig.update_traces(textinfo='percent + label')
fig.show()


fig = px.pie(data_frame=Grouped_data , names='platform' , values='likes' , hole=0.4 , color_discrete_sequence=px.colors.qualitative.Bold_r)
fig.update_traces(textinfo='percent + label' , pull=[0,0.2,0])
fig.show()













