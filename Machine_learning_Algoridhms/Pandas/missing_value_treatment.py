import pandas as pd

df= pd.read_csv("weight-height.csv")
mean=df["Height"].mean()
median=df["Height"].median()
mode=df["Height"].mode()
# print(mean)
# print(median)
# print(mode)
d=df["Height"].fillna(mean)
print(d)