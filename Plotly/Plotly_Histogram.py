import pandas as pd 
import plotly.express as px

df = pd.read_csv('social_media_engagement.csv')

fig = px.histogram(data_frame =df , x='comments' , template='simple_white' , width=700 , nbins=30)
fig.show()

fig = px.histogram(data_frame =df , x='comments' , template='simple_white' , width=700)
fig.show()

