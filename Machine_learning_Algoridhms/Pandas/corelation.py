# import pandas as pd
# import numpy as np
# from scipy.stats import pearsonr
#
# df=pd.read_csv("weight-height.csv")
# print((df.shape))
# x=df["Height"]
# y=df["Weight"]
# cor=np.corrcoef(x,y)
# print(cor)
# cor1=pearsonr(x,y)
# print(cor1)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv("data.csv")
print(df.shape)
print(df.head(5).to_string())

x = df.iloc[:,2:6]
# print(x.head().to_string())
y = df.iloc[:,1]
# print(y.head().to_string())

# Train data

x_train = x[:200]
y_train = y[:200]

# Test data

x_test = x[200:500]
y_test = y[200:500]

# Create model

logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
y_predict = logmodel.predict(x_test)

# Confusion Matrix
con_matrix = confusion_matrix(y_test,y_predict)
print(con_matrix)

# Print Report

print(classification_report(y_test,y_predict))

print(keyword)
