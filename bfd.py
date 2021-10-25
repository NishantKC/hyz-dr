import pandas as pd
data =pd.read_csv("newdata.csv")
import plotly.figure_factory as ff
average = data["average"].tolist()
fig=ff.create_distplot([data["average"].tolist()],["fhs"],show_hist=False)
#fig.show()

import random
import statistics
meanlist=[]
for i in range(0,1000):
    d=[]
    for j in range(0,100):
        idx=random.randint(0,len(average)-1)
        value=average[idx]
        d.append(value)
    mean=statistics.mean(d)
    meanlist.append(mean)
fig=ff.create_distplot([meanlist],["fhs"],show_hist=False)
fig.show()

pm=statistics.mean(average)
sm=statistics.mean(meanlist)
print(pm,sm)

ps=statistics.stdev(average)
ss=statistics.stdev(meanlist)
print(ps,ss)