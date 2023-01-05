import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("https://www.w3schools.com/python/pandas/data.csv")
dd=pd.DataFrame(a)
print(dd)

aa=dd.corr()
print(aa)

aa.plot()
ply.show()

y=aa['Maxpulse'].tolist()
print(y)
mylabels=['Duration','Pulse','Maxpulse','Calories']
plt.pie(y, labels=mylabels)
plt.show
