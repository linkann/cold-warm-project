import numpy as np
import pandas as pd
from scipy.spatial import KDTree
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

#pts = np.array([(1, 3), (2, 1), (3, 8), (4, 10), (3, 4), (5, 3), (7, 1), (7, 4), (8, 5), (11, 2), (5, 6), (2, 9), (1, 5), (2, 4), (6, 10), (2, 3)])


pts = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(1, 2))
pts2 = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(0))
#print("pts2: ", pts2[2])
#print("shape:", pts.shape)
#print("pts:", pts)
print("======================")
#X = pts[0:3]
#print("pts : ", pts)

#df1 = pd.read_csv('weather.csv', sep=',', header=None, skiprows=[0], usecols=(1, 2))
#print(df1.values)
#print(df1.shape)
#print("===============")
#df2 = pd.read_csv('weather.csv', sep=',', header=None, skiprows=[0], usecols=(0,))
#print(df2[2])
#print(df2.shape)

T = KDTree(pts)
idx = T.query_ball_point([1, 8], r=1)
#######################################################
# terminal창에 뜨는 좌표값이 반지름 3 반경 안에 드는 좌표값들임 #
#######################################################
print("idx : ", idx)
print("pts2: ", pts2[idx])
print(pts[idx])
#print("idx SHAPE : ", np.shape(idx))
#print("idx INDEX!! : ", idx[1])
#print("날씨!! : ", df2[idx[1]])
print("=======================================================")
print("=======================================================")
print("=======================================================")
#print(df2[idx[0]])

########################
#    이하 그래프 샘플     #
########################
point = [1, 8]
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(Circle(point, 3, color='r', fill=False))
X, Y = [p[0] for p in pts], [p[1] for p in pts]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c='r')
plt.show()

