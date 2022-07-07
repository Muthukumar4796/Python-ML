import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("weight-height.csv")
# print(df)

mx_df=df[df["Gender"] == 'Male']
x=mx_df["Height"].tolist()
y=mx_df["Weight"].tolist()
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("HeightWeight")
plt.hist([x,y])
# plt.show()

fx_df=df[df["Gender"] == 'Female']
x1=fx_df["Height"].tolist()
y1=fx_df["Weight"].tolist()
print(x1)
print(y1)
plt.hist([x1,y1])
plt.show()