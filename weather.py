import urllib.request

import json

import datetime

import csv


url = 'http://api.openweathermap.org/data/2.5/forecast?id=1835847&APPID=d32e43d4745e9c09c21034f715c43287'

u = urllib.request.urlopen(url)

data = u.read()



j = json.loads(data)





name = j["city"]["name"]

print ("City name:")

print (name)

print ("\n")



dt = j["list"][0]["dt"]

print ("Data receiving time:")

strdt = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')

print (strdt)

print ("\n")





main = j["list"][0]["main"]


today1 = j["list"][1]["main"]
today2 = j["list"][2]["main"]
today3 = j["list"][3]["main"]
today4 = j["list"][4]["main"]
today5 = j["list"][5]["main"]
today6 = j["list"][6]["main"]
today7 = j["list"][7]["main"]


temp = main["temp"]
todaytemp1 = today1["temp"]
todaytemp2 = today2["temp"]
todaytemp3 = today3["temp"]
todaytemp4 = today4["temp"]
todaytemp5 = today5["temp"]
todaytemp6 = today6["temp"]
todaytemp7 = today7["temp"]

today = [int(temp), int(todaytemp1), int(todaytemp2), int(todaytemp3), int(todaytemp4), int(todaytemp5), int(todaytemp6), int(todaytemp7)]

today.sort()

print(today)

print ("\n")

dtr = today[7]-today[0]
strdtr = str(dtr)



print ("temperature:")

print (int(temp) - 273.15)

windchill = int(temp) - 273.15

strwindchill=str(windchill)


print ("\n")




print ("daily temperature range: ")
print(dtr)
print("\n")


print("windchill: ")
print(windchill)

print("\n")

row = [strdt, strdtr, strwindchill]

csvfile = open("current.csv", "w", newline="")

csvwriter = csv.writer(csvfile)

csvwriter.writerow(row)

#csvfile.close()


row.clear()


weather = j["list"][0]["weather"]

main = weather[0]

print (main["main"])

print (main["description"])
