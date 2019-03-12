import urllib.request
import json
import datetime
import csv

url = 'http://api.openweathermap.org/data/2.5/forecast?id=1835847&APPID=d32e43d4745e9c09c21034f715c43287'
u = urllib.request.urlopen(url)
data = u.read()

j = json.loads(data)
name = j["city"]["name"]

print("City name:")
print(name)
print("\n")

dt = j["list"][0]["dt"]
print("Data receiving time:")
strdt = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')
print(strdt)
print("\n")

main = j["list"][0]["main"]
temp = main["temp"]
print("temperature:")
print(int(temp) - 273.15)
windchill = int(temp) - 273.15
strwindchill = str(windchill)
print("\n")

temp_max = main["temp_max"]
print("maximum temperature:")
print(int(temp_max)-273.15)
print("\n")

temp_min = main["temp_min"]
print("minimum temperature:")
print(int(temp_min)-273.15)
print("\n")

dtr = int(temp_max)-int(temp_min)
strdtr = str(dtr)
print(strdt)
print(dtr)
print(windchill)

row = [strdt, strdtr, strwindchill]
csvfile = open("current.csv", "w", newline="")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(row)

row.clear()
weather = j["list"][0]["weather"]
main = weather[0]
print(main["main"])
print(main["description"])
