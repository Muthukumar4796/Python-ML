import pandas as pd
# list=[1,2,3,4]
# m=pd.Series(list)
# x=m.tolist()
# print(x)

# +,-,*,/ the series
# import pandas as pd
# list1=[2,3,4,5]
# list2=[6,7,8,9]
# df=list1+list2
# # print(df)

# compare the series
# import pandas as pd
# list1=[2,3,4,5]
# list2=[6,3,8,9]
# x=pd.Series(list1)
# y=pd.Series(list2)
# # print(x==y)
# print(x<=y)
# print(x>=y)

# Converts dic into pandas series
# import pandas as pd
# x={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# y=pd.Series(x)
# print(y)

# Write a Pandas program to change the data type of given a column or a Series
# import pandas as pd
# list=[6,7,"py",9]
# x=pd.Series(list)
# print(x)
# y=pd.to_numeric(x,errors='coerce')
# print(y)

# index the column in  pandas
# import pandas as pd
# d={"x":[1,2,3,4,5],"y":[1,3,5,6,8],"z":[9,6,4,3,1]}
# df=pd.DataFrame(data=d)
# # print(df)
# df1=df.iloc[1:,1]
# print(df1)

# pandas series converts into array
# import pandas as pd
import numpy as np
x=[6,7,"py",9,10.21]
y=np.array(x)
print(y)
