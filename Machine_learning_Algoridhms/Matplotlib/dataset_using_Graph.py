import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("country_population.csv")
# print(df)
x_df=df.drop(["Country Code","Indicator Name","Indicator Code","Country Name"],axis=1)
x=x_df.columns.tolist()
print(x)

y_df=df.iloc[0:1,4:]
y=y_df.values[0]
# print(type(y))
# plt.locator_params(axis='x', nbins=len(x)/2)  # set divisor
plt.plot(x,y)
plt.xticks(x[::5],rotation=90) # set divisor

plt.show()
