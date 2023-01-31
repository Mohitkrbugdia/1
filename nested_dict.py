import pandas as pd
n=int(input('enter no. of students'))
dict={}
for i in range(1,n+1):
    dict.update({i:{'name':input('enter name'),
          'roll no.':int(input('enter roll no.')),
          'subject 1':int(input('enter marks in sub. 1:')),
          'subject 2':int(input('enter marks in sub. 2:')),
          'subject 3':int(input('enter marks in sub. 3:'))}})
    print(dict)
    a=pd.DataFrame(dict)
    print(a)
