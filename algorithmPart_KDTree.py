import numpy as np
from scipy.spatial import KDTree
# from matplotlib import pyplot as plt
# from matplotlib.patches import Circle

today_windchill = np.genfromtxt('current.csv', dtype=None, delimiter=',', usecols=(1))
today_DTR = np.genfromtxt('current.csv', dtype=None, delimiter=',', usecols=(2))
radius = 0.7

windchill_DTR = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(1, 2))
dateArray = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(0))

T = KDTree(windchill_DTR)
address_rare = T.query_ball_point([today_windchill, today_DTR], r=radius)

if len(address_rare) > 6:
    address = address_rare[0:5]
else:
    address = address_rare

print("dateArray: ", dateArray[address])

#################
# 이하 그래프 샘플 #
#################
# point = [today_windchill, today_DTR]
# fig = plt.figure()
# ax = fig.add_subplot(111, aspect='equal')
# ax.add_patch(Circle(point, radius, color='r', fill=False))
# X, Y = [p[0] for p in windchill_DTR], [p[1] for p in windchill_DTR]
# plt.scatter(X, Y)
# plt.scatter([point[0]], [point[1]], c='r')
# plt.show()
