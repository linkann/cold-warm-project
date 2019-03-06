import numpy as np
from scipy.spatial import KDTree
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

# today_windchill(오늘의 체감온도), today_DTR(오늘의 일교차), radius : 실행을 위해 각각 1, 8, 0.5로 임의의 값 지정함.
# today_windchill 과 today_DTR 은 JSON 으로부터 value 넘겨 받아야 함.
today_windchill = 1
today_DTR = 8
radius = 0.5

windchill_DTR = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(1, 2))
dateArray = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(0))

T = KDTree(windchill_DTR)
address = T.query_ball_point([today_windchill, today_DTR], r=radius)

print("address : ", address)
print("\n")
print("dateArray: ", dateArray[address])
print("specific dateArray example: ", dateArray[address[2]])
print("\n")
print("windchill_DTR : \n", windchill_DTR[address])

#################
# 이하 그래프 샘플 #
#################
point = [today_windchill, today_DTR]
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(Circle(point, radius, color='r', fill=False))
X, Y = [p[0] for p in windchill_DTR], [p[1] for p in windchill_DTR]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c='r')
plt.show()
