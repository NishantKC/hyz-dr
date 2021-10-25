import pandas as pd
import plotly.express as px
df=pd.read_csv("bye.csv")
graph=px.scatter(df,x="Coffee in ml",y="sleep in hours")
graph.show()
corr=df.corr()
print(corr)