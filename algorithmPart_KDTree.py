import numpy as np
from scipy.spatial import KDTree
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

# today_windchill(오늘의 체감온도), today_DTR(오늘의 일교차) : 실행을 위해 각각 3, 8 로 임의의 값 지정함.
# today_windchill 과 today_DTR 은 JSON 으로부터 value 넘겨 받아야 함.
# radius 는 0.7 로 결정됨.
today_windchill = 3
today_DTR = 8
radius = 0.7

windchill_DTR = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(1, 2))
dateArray = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(0))

T = KDTree(windchill_DTR)
address_rare = T.query_ball_point([today_windchill, today_DTR], r=radius)

if len(address_rare) > 6:
    address = address_rare[0:5]
else:
    address = address_rare

# 추천 날짜는 dateArray[address]에 들어 있음.
print("dateArray: ", dateArray[address])
print("\n사용 예시) 첫 번째 날짜 : ", dateArray[address[0]])

# address_rare : 점 (today_windchill, today_DTR)의 이웃인 점들이 실제 weather1.csv 파일에서는 몇 번째 행에 있는지에 대한 주소 리스트.
# print("address_rare : ", address_rare)
# address : address_rare 에서 0번지부터 4번지까지의 값을 저장한 리스트.
# print("address : ", address)
# windchill_DTR : 점 (today_windchill, today_DTR)의 이웃인 점들의 X 좌표값, Y 좌표값들의 2차원 배열
# print("windchill_DTR : \n", windchill_DTR[address])

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
