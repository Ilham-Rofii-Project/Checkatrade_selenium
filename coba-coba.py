import pandas as pd

df=pd.DataFrame({'title':[],
                 'link':[],
                 'tag':[]})
df.to_csv('result.csv',index=False)

df=pd.DataFrame({'title':'hehe',
                 'link':'hehe',
                 'tag':'hehe'})
df.to_csv('result.csv',index=False,mode='a',header=False)