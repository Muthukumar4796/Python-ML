# import pandas as pd
# df1=pd.read_csv('nba.csv')
# df2=pd.read_csv('Nba_2.csv')
#
# MDF=pd.merge(df1,df2,on="Name")
# print(MDF)
# ndf=df1.drop_duplicates("Name")
# print((ndf))

# ndf=df1["Age"].mode()
# print(ndf)
# import random
# print(random.randint(1,6))
# while random==random:
#     random+random
#     print(random)


# from random import randint
# sum = 0
#
#
# def roll_dice():
#     dice1 = randint(1, 6)
#     dice2 = randint(1, 6)
#     print("dice1-", dice1, "dice2-", dice2)
#     global sum
#     if (dice1 != dice2):
#         sum += max(dice1, dice2)
#         roll_dice()
#     else:
#         sum += dice1 + dice2
#         print("Toal sum", sum)
#         # return sum
#
#
# roll_dice()

# skewness

# import pandas as pd
# df=pd.read_csv('nba.csv')
# print(df.skew(axis=0,skipna=True))

# Normal distribution
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
#
# x= np.arange(-5,5,0.001)
# y=np.mean(x)
# print(y)
# x=x.std()
# print(x)
# print(x)
# norm probablity distribution
# plt.plot(x,norm.pdf(x,0,1))
# p=norm.pdf(x,0,1)
# print(p)
# plt.show()

# import math
# n= float(input("Enter the number:"))
# result= n**0.5
# print("Square root of",n,"is:",result)

# g=n/2
# for i in range (0,100):
#     a=((g-(g**2-n/2g)))
#     a=g
#     print("Square root of",n,"is:")


# std deviation and variation
import math
import numpy as np
import pandas as pd

df=[600,470,170,430,300]
add=sum(df)
total=len(df)
mean=add/total
# print(mean)

z=[]
for i in df:
    k=(i-mean)**2
    z.append(k)
print(z)

sig_sq= sum(z)/5
print(sig_sq)

sig= math.sqrt(sig_sq)
print(sig)

a=np.std(df)
print(a)
series=pd.Series(df)
s=series.std(ddof=0)
print(s)