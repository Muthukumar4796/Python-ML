# import pandas as pd
# df=pd.read_csv('tested.csv')
# # print(df.to_string())
# # df=pd.DataFrame({"Gender":["male", "male", "female", "male"],
# #                 "Survived":[0,0,1,1]})
# #
# # prob = df.loc[df['Sex'] == 'male', 'Survived'].mean()
# # print(prob)
# # prob_percent = df.groupby('Sex')['Survived'].mean()
# # print(prob_percent)
# prob_percent = df.groupby('Age')['Survived'].mean()
# print(prob_percent)

# import pandas as pd
# from scipy import stats
# import matplotlib.pyplot as plt
#
# df= pd.DataFrame(columns=['No','quantity'], data=[[1,100.0],[2,102.3],[3,301.3],[4,101.3],[5,101.3],[6,120.3]])
# mu=df.quantity.mean()
# print(mu)
#
# sig=df.quantity.std()
# print(sig)
#
# z=df['z_score']=stats.mstats.zscore(df.quantity)
# print(z)

# prob=df['quantity'].apply(lambda x: stats.norm(mu,sig).pdf(x) if x > mu else 1 - stats.norm(mu,sig).pdf(x))
# print(prob)
#
# prob_percent = prob.apply(lambda x: x*100)
# print(prob_percent)
# for idx,row in df.iterrows():
#     # print(stats.norm.pdf((row.quantity),mu,sig))
#     if row.quantity < mu:
#         df.at[idx,'prob'] = 1- (stats.norm(mu,sig).pdf(row.quantity))
#         print(df.at[idx,'prob'])
#     else:
#         df.at[idx,'prob'] = stats.norm(mu, sig).pdf(row.quantity)

#odd ratio
# fisherexacttable

from scipy import stats

odds = stats.fisher_exact([[8,4],[2,6]])
print(odds)
