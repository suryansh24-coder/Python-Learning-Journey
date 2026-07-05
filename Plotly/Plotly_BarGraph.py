import pandas as pd 
import plotly.express as px

df = pd.read_csv("Social_Media.csv")
fig = px.bar(df , x='Date' , y='Engagement_Score',template='simple_white' , width=600)
fig.show()

likes_data = df.groupby('Post_Type')['Likes'].sum().reset_index()
print(likes_data.to_string())
fig1 = px.bar(likes_data , x='Post_Type' , y='Likes',template='simple_white' , width=600)
fig1.show()

fig2 = px.bar(likes_data , y='Post_Type' , x='Likes', orientation='h',template='simple_white' , width=600)
fig2.show()

likes_data2 = df.groupby('Post_Type')['Likes'].sum().reset_index().sort_values('Likes')
print(likes_data2.to_string())
fig3 = px.bar(likes_data2 , y='Post_Type' , x='Likes', orientation='h',template='simple_white' , width=600)
fig4 = px.bar(likes_data2 , x='Post_Type' , y='Likes',template='simple_white' , width=600)
fig3.show()
fig4.show()

avg_data = df.groupby('Platform')[['Likes','Engagement_Score']].mean().reset_index()
print(avg_data.to_string())
fig5 = px.bar(avg_data , x = 'Platform' , y=['Likes','Engagement_Score'],barmode='stack', template='simple_white' , title='Average value')
fig5.show()

c = { 
     'Likes' : '#0d0887', 
      'Engagement_Score' : '#46039f'
      }
fig6 = px.bar(avg_data , x = 'Platform' , y=['Likes','Engagement_Score'],barmode='stack', template='simple_white' , title='Average value' , color_discrete_map = c  )
fig6.show()
c = { 
     'Likes' : 'cyan', 
     'Engagement_Score' : 'hotpink'
    }
fig7 = px.bar(avg_data , x = 'Platform' , y=['Likes','Engagement_Score'],barmode='group', template='simple_white' , title='Average value', color_discrete_map=c)
fig7.show()

avg_data['negative_c'] = avg_data['Engagement_Score'] * -1
fig8 = px.bar(avg_data , x=['Likes','negative_c'] , y='Platform' ,orientation = 'h' , barmode='relative' , template='simple_white')
fig8.show()



 
 
 
 