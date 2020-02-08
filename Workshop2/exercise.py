import numpy as np
import pandas as pd
print('-------')
a=[1,2,3,4,5,6]
a_1=a[-3:]
a.reverse()
a_2=a
a.reverse()
a_3=[x**2 for x in a]
print(a_1,a_2,a_3)

print('--------')
b=[1,2,5,3,2,0]
b=np.array(b)
print(b)
print('mean of b:',b.mean())
b=b.reshape(2,3)
print(b)
print('mean each row:',b.mean(axis=1))
print('mean each column:',b.mean(axis=0))
print('third column of b:',b[:,2])
print("square of b:",b**2)

print('---------')
df=pd.read_csv("./starbucks.csv")
print("average calories:",df["Calories"].mean())
print("total number of categories:",len(df["Beverage_category"].unique()))
group=df.groupby("Beverage_category")
print(group["Calories"].mean())
print("beverage preparation which includes the most sugar:")
print(df[df["Sugars (g)"]==df["Sugars (g)"].max()]["Beverage_prep"])
print('---------')

def getint(name):
   return int(name.split('%')[0])
df2=df
df2["Calcium (% DV)"]=df["Calcium (% DV)"].apply(getint)
group_beverage=df2.groupby("Beverage")
print(group_beverage["Calcium (% DV)"].mean())

print('-------------')
a=df["Protein (g)"].to_numpy()






