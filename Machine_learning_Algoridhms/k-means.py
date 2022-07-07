import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.DataFrame({
    'x':[12,20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,69,72,24,15,6],
    'y':[39,36,30,52,54,45,55,59,46,55,59,63,70,66,63,58,23,14,8,19,7,24]
})

kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
colmap = {1:'r',2:'b',3:'g',4:'k'}
label = kmeans.predict(df)
centroids = kmeans.cluster_centers_
print(centroids)
fig = plt.figure(figsize=(3,3))
colors = map(lambda x:colmap[x+1],label)
colors1 = list(colors)
plt.scatter(df['x'],df['y'],color = colors1,alpha = 0.5,edgecolor = 'k')
for idx , centroids in enumerate(centroids):
    plt.scatter(*centroids,color = colmap[idx+1])
plt.xlim(0,85);plt.ylim(0,85)
plt.show()
# print(centroids)