import pandas as pd
import plotly.express as px
df=pd.read_csv("hi.csv")
graph=px.scatter(df,x="Temperature",y="Ice-cream Sales")
graph.show()
corr=df.corr()
print(corr)