import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("https://www.w3schools.com/python/pandas/data.csv")
dd=pd.DataFrame(a)
print(dd)

d=dd.Duration[:10]
#print(d)
ss=d.tolist()
a1=d.mean()
print("meanduration:",a1)

d1=dd.Pulse[:10]
#print(d1)
ss1=d1.tolist()
a2=d1.mean()
print("meanpulse:",a2)

d3=dd.Maxpulse[:10]
#print(d3)
ss3=d3.tolist()
a3=d3.mean()
print("meanmaxpulse:",a3)

d4=dd.Calories[:10]
#print(d4)
ss4=d4.tolist()
a4=d4.mean()
print("meancalories:",a4)

meanlist=[a1,a2,a3,a4]
print('meanlist:',meanlist)

mylabels=['Duration','Pulse','Maxpulse','Calories']
plt.pie(meanlist, labels=mylabels)
plt.show
