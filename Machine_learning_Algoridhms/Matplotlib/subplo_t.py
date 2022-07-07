# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# df=pd.read_csv("country_population.csv")
# # print(df)
# x_df=df.drop(["Country Code","Indicator Name","Indicator Code","Country Name"],axis=1)
# x=x_df.columns.tolist()
# print(x)
#
# y_df=df.iloc[0:1,4:]
# y=y_df.values[0]
# # print((y))
# plt.subplot(2,2,1)
# plt.plot(x,y)
#
# y1_df=df.iloc[1:2,4:]
# y1=y_df.values[0]
# plt.subplot(2,2,2)
# plt.plot(x,y1)
#
# plt.xticks(x[::5],rotation=90) # set divisor
#
# plt.show()
#
#
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# df=pd.read_csv("country_population.csv")
# # print(df)
# x_df=df.drop(["Country Code","Indicator Name","Indicator Code","Country Name"],axis=1)
# x=x_df.columns.tolist()
# print(x)
#
# y_df=df.iloc[0:1,4:]
# y=y_df.values[0]
# # print((y))
# plt.subplot(2,2,1)
# plt.plot(x,y)
#
# y1_df=df.iloc[1:2,4:]
# y1=y_df.values[0]
# plt.subplot(2,2,2)
# plt.plot(x,y1)
#
# plt.xticks(x[::5],rotation=90) # set divisor
#
# plt.show()

#Scatterplot &histogram &pie chart

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df=pd.read_csv("weight-height.csv")
# # print(df)
#
# mx_df=df[df["Gender"] == 'Male']
# x=mx_df["Height"].tolist()
# y=mx_df["Weight"].tolist()
# print(x)
# print(y)
# plt.xlabel("Years")
# plt.ylabel("Population")
# plt.title("Country population")
# plt.scatter(x,y)
# # plt.hist(x,y)
#
# fx_df=df[df["Gender"] == 'Female']
# x1=fx_df["Height"].tolist()
# y1=fx_df["Weight"].tolist()
# print(x1)
# print(y1)
# # plt.scatter(x1,y1)
# plt.hist(x1,y1)
# plt.show()

x={"value":[100,200,300,400,500],"vehicle":["auto","bus","bike","boat","aeroplane"]}
plt.pie(x["value"],labels=x["vehicle"])
plt.legend(x)
plt.show()