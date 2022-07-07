import pandas as pd
df = pd.read_csv("salary.csv")
df.head()
print(df.to_string())

inputs= df.drop("Salary_more_then_10k",axis='columns')
target=df["Salary_more_then_10k"]

from sklearn.preprocessing import LabelEncoder

le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()

input['company_n']= le_company.fit_transform(input['Company'])
input['job_n']= le_company.fit_transform(input['Job'])
input['degree_n']= le_company.fit_transform(input['Degree'])
print(input.to_string())
input_n=input.drop(['company','job','degree'],axis=1)
print(input_n)