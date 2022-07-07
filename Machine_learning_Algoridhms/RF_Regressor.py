import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

data= pd.read_csv("random_forest_regressor.csv")
print(data)

X=data.iloc[:,:7].astype(int)
print(X.to_string())

Y=data.iloc[:,7].astype(int)
print(Y.to_string())

X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.3,random_state=1)
regressor= RandomForestRegressor(n_estimators=10)
regressor=regressor.fit(X_train,Y_train)
Y_pred=regressor.predict(X_test).astype(int)
print(Y_test)
print(Y_pred)

print(("Accuracy:",metrics.accuracy_score(Y_test,Y_pred)))

from matplotlib import pyplot as plt
from sklearn import tree

fig=plt.figure()

tree.plot_tree(regressor.estimators_[5])
plt.show()

tree.plot_tree(regressor.estimators_[0])
plt.show()


