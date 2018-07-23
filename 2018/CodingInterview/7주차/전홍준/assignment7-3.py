city =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
city2 = []
time = 0
temp = []
cacheSize=int(input())

for i in range(len(city)):
    city2.append(city[i].upper())

for i in city2:
    if len(temp) < cacheSize:
        if i in temp:
            temp.pop(0)
            temp.append(i)
            time += 1
        else:
            time += 5
            temp.append(i)
    elif len(temp) == cacheSize:
        if i in temp:
            temp.pop(0)
            temp.append(i)
            time += 1
        else:
            temp.pop(0)
            temp.append(i)
            time += 5

print(time)