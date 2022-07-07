import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,5,8,13,21,34,55,89])
# x2 = np.array([2,3,4,5,6,5,4,3,2,3,5,7,8,])
# y2 = np.array([1,9,8,6,4,5,7,8,3,5,6,7,2])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# plot label x,y
plt.xlabel("Average Pulse", fontdict=font1)
plt.ylabel("Calorie Burnage", fontdict=font2)

# plot title
plt.title("Sports Watch Data", fontdict=font1)


# plt.plot(xpoints,ypoints)

# implied markers in our plot
plt.plot(x,y,marker="o")

# implied line style
# plt.plot(x,y,linestyle="-.")
#
# implied line color
# plt.plot(y,color = 'r')

# implies line width
# plt.plot(x1,y1,x2,y2, linewidth = '5')

plt.show()
