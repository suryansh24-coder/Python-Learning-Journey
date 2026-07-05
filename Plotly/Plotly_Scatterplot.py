import pandas as pd 
import plotly.express as px 

pf = pd.read_csv('social_media_engagement.csv')
fig = px.scatter(pf, x='likes' , y='comments' ,template='seaborn' ,width=700)
fig.show()

fig1 = px.scatter(pf, x='likes' , y='comments' ,template='seaborn' ,width=700 , color='platform')
fig1.show()

fig2 = px.scatter(pf, x='likes' , y='comments' , size='likes' ,template='seaborn' ,width=700)
fig2.show()

fig3 = px.scatter_3d(pf, x='likes' , y ='comments', z='shares')
fig3.show()

fig4 = px.scatter_3d(pf, x='likes' , y ='comments', z='shares' , color='platform' , size='likes')
fig4.show()

fig5 = px.scatter_matrix(pf , dimensions=['likes','comments','shares'] , title='scatter matrix')
fig5.show()



 
 