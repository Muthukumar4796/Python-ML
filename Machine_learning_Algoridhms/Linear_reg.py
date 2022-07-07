import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("headbrain.csv")
print(df)

X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values

## to find the mean of the X and Y
Mean_X = np.mean(X)
Mean_Y = np.mean(Y)

m = len(X)

numera = 0
denami = 0

for i in range(m):
   numera+=(X[i]-Mean_X)*(Y[i]-Mean_Y)
   denami +=(X[i]-Mean_X)**2
M = numera / denami
print("The value of the M is ","%.2f"%round(M,2))

C = Mean_Y -(M*Mean_X)
print("The C value is ","%.2f"%round(C,2))

Y_1 = M*X+C
print(Y_1)

## ploting the graph
plt.scatter(X,Y,color = 'Blue',label ="Scatter plots")
plt.plot(X,Y_1,color= 'red',label = "Line of Regression")
plt.xlabel ("Head Size in cm^3")
plt.ylabel ("Brain size in grams")
plt.legend()
plt.show()

## to find the R2 value is
Numerator = 0
Denaminator = 0

for x in range(m):
   Numerator+=(Y_1[x]-Mean_Y)**2
   Denaminator+=(Y[x]-Mean_Y)**2

R_2 = Numerator / Denaminator
print("The R^2 value of the given function is ","%.2f"%round(R_2*100,2),"%")

