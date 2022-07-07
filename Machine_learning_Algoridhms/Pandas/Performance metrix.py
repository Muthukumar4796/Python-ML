import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report


df=pd.read_csv("data.csv", encoding_errors="ignore")
print(df.shape)

x=df.iloc[:,2:6]
y=df.iloc[:,1]
print(x)

# training the data
x_train=x[:200]
y_train = y[:200]

# test the data
x_test=x[200:500]
y_test=y[200:500]

# logistic model
log_model=LogisticRegression()
log_model.fit(x_train , y_train)
y_predict=log_model.predict(x_test)
# plt.scatter(x_train, y_train, color = 'blue')
# plt.plot(x_train, y.predict(x_test), color = 'red')
#
# plt.show()
print(y_predict)

# Confusion Matrix
con_matrix = confusion_matrix(y_test,y_predict)
print(con_matrix)

# Print Report

print(classification_report(y_test,y_predict))