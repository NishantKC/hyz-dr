import pandas as pd
import plotly.express as px
df=pd.read_csv("tv.csv")
graph=px.scatter(df,x="Size of TV",y="Average time spent watching TV in a week (hours)")
graph.show()
corr=df.corr()
print(corr)