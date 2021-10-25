import random
data=[]
for i in range(0,100):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    data.append(d1+d2)
import plotly.figure_factory as ff
fig=ff.create_distplot([data],["fhs"],show_hist=False)
fig.show()