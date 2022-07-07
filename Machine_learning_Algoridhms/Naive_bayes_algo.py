import pandas as pd
df = pd.read_csv('tested.csv')
df.head()

df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
df.head()

inputs = df.drop('Survived',axis='columns')
target = df.Survived

dummies = pd.get_dummies(inputs.Sex)
dummies.head(3)

inputs = pd.concat([inputs,dummies],axis='columns')
inputs.head(3)

inputs.drop(['Sex','male'],axis='columns',inplace=True)
inputs.head(3)

inputs.columns[inputs.isna().any()]
Index(['Age'], dtype='object')

inputs.Age[:10]

inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.head()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)
GaussianNB(priors=None, var_smoothing=1e-09)
model.score(X_test,y_test)
X_test[0:10]
