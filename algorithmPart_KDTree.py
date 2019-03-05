import numpy as np
from scipy.spatial import KDTree
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

pts = np.array([(1, 3), (2, 1), (3, 8), (4, 10), (3, 4), (5, 3), (7, 1), (7, 4), (8, 5), (11, 2), (5, 6), (2, 9), (1, 5), (2, 4), (6, 10), (2, 3)])

T = KDTree(pts)
idx = T.query_ball_point([5, 5], r=3)
#######################################################
# terminal창에 뜨는 좌표값이 반지름 3 반경 안에 드는 좌표값들임 #
#######################################################
print (pts[idx])


########################
#    이하 그래프 샘플     #
########################
point = [5,5]
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(Circle(point, 3, color='r', fill=False))
X, Y = [p[0] for p in pts], [p[1] for p in pts]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c='r')
plt.show()