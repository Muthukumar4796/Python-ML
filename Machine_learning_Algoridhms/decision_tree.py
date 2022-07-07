import pandas as pd
import numpy as np

df = pd.DataFrame([['google','sales execute','degree',0],
                   ['google','sales execute','masters','0'],
                   ['google','business manager','bachelors',1],
                   ['google','business manager','masters',1],
                   ['google','computer programmer','bachelors',0],
                   ['google','computer programmer','masters',1],
                   ['abc pharma','sales execute','masters',0],
                   ['abc pharma','computer programmer','bachelors',0],
                   ['abc pharma','business manager','bachelors',0],
                   ['abc pharma','business manager','masters',1],
                   ['facebook','sales execute','bachelors',1],
                   ['facebook','sales execute','masters',1],
                   ['facebook','business manager','bachelors',1],
                   ['facebook','business manager','masters',1],
                   ['facebook','computer programmer','bachelors',1],
                   ['facebook','computer programmer','masters',1]],
                  columns=['Company','Job','Degree','Salary_more_then_10k'])
print(df)
df.to_csv('Salary.csv')

import pandas as pd
import numpy as np

Data = pd.read_csv('Salary.csv')
input = Data.drop(['Salary_more_then_10k'],axis = 1)
target = Data['Salary_more_then_10k']

from sklearn.preprocessing import LabelEncoder # LabelEncoder is used for string purpose only...
# Is data is numeric we can process the data in StandardScaler module in pre processing.
le_company = LabelEncoder()

input['company'] = le_company.fit_transform(input['Company'])
input['job'] = le_company.fit_transform(input['Job'])
input['degree'] = le_company.fit_transform(input['Degree'])
print(input.to_string())
input_n= input.drop(['Company','Job','Degree'],axis = 1)
print(input_n)
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(input_n,target)

score = tree.score(input_n,target)*100
print(score,"%  Having good percentage")
Out = tree.predict([[2,2,1,1]])
print(Out)
if Out == 0:
    print('The person salary below 10k ')
else:
    print("The person salary is beyond the 10k")