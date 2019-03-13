import numpy as np
from scipy.spatial import KDTree
import glob
from PIL import Image
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

def calculateSize(files):
    size_x = []
    size_y = []
    for file in files:
        image = Image.open(file)
        size_x.append(image.size[0])
        size_y.append(image.size[1])

    x_min = min(size_x)
    y_min = min(size_y)
    total_x_size = y_min * len(files)
    return x_min, y_min, total_x_size

def resizeTomin(files, x_min, y_min, y_size):
    file_list = []
    for file in files:
        image = Image.open(file)
        resized_file = image.resize((x_min, y_min))
        file_list.append(resized_file)
    return file_list, y_size, x_min, y_min

def imageMerge(file_list, y_size, x_min, y_min, i):
    new_image = Image.new("RGB", (x_min, y_size), (256, 256, 256))
    for index in range(len(file_list)):
        area = (0, (index * y_min), x_min, (y_min * (index + 1)))
        new_image.paste(file_list[index], area)
    new_image.show()
    tempString = "C:/Users/SOOKMYUNG/Desktop/today_clothes_" + str(i) + ".png"
    new_image.save(tempString, "PNG")

#today_windchill = np.genfromtxt('current.csv', dtype=None, delimiter=',', usecols=(2))
#today_DTR = np.genfromtxt('current.csv', dtype=None, delimiter=',', usecols=(1))
today_windchill = 1
today_DTR = 8
radius = 0.7

windchill_DTR = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(1, 2))
dateArray = np.genfromtxt('weather1.csv', dtype=None, delimiter=',', skip_header=1, usecols=(0))

T = KDTree(windchill_DTR)
address_rare = T.query_ball_point([today_windchill, today_DTR], r=radius)

if len(address_rare) > 6:
    address = address_rare[0:2]
else:
    address = address_rare

print("dateArray: ", dateArray[address])

## 파일 이름 설정
length = len(address)
length = 2
temparr = [0, 1, 2, 3, 4, 5]
for i in range(length):
    temparr[i] = dateArray[int(address[i])]
print("===========================================================================")

for i in range(length):
    print("if문 i : ", i)
    recommendDate = temparr[i]
    print("recommendDate : ", recommendDate)
    top = str(recommendDate) + "_top.png"
    bottom = str(recommendDate) + "_bottom.png"
    shoes = str(recommendDate) + "_shoes.png"
    jacket = str(recommendDate) + "_jacket.png"

    ## 절대 경로 설정
    path = "C:/Users/SOOKMYUNG/Desktop/cold-warm-project/"
    # 출력이미지 변수 설정
    bottom_img = img.imread(path + bottom)
    shoes_img = img.imread(path + shoes)
    jacket_img = img.imread(path + jacket)
    top_img = img.imread(path + top, 0)

    target_dir = "C:/Users/SOOKMYUNG/Desktop/cold-warm-project/"
    files = glob.glob(target_dir + "*.*")
    x_min, y_min, y_size = calculateSize(files)
    file_list, x_size, x_min, y_min = resizeTomin(files, x_min, y_min, y_size)
    imageMerge(file_list, y_size, x_min, y_min, i)
