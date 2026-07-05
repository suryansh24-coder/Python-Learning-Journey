import pandas as pd 
import plotly.express as px 
import seaborn as sns 

df = pd.read_csv('social_media_engagement.csv')
df2 = sns.load_dataset('tips')
fig = px.box(data_frame=df , x='likes' , template='simple_white')
fig.show()

fig2 = px.box(data_frame=df , x='total_bill', template='simple_white')
fig2.show()

fig3 = px.box(data_frame = df , x='total_bill', template='simple_white')

fig3 = px.violin(data_frame = df , x='total_bill', template='simple_white')

