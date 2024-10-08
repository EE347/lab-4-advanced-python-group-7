import csv
import matplotlib.pyplot as plt
from datetime import datetime


plots = {}

with open('task9.csv', 'r') as file:        
    csvfile = csv.reader(file)
    headers = next(csvfile)

    data = {}

    for title in headers:
        data[title] = []

    for row in csvfile:
        for index, title in enumerate(headers):
            if title != headers[0]:
                data[title].append(float(row[index]))
            else:
                data[title].append(row[index])

for i in range(len(data[headers[0]])):
    data[headers[0]][i] = datetime.strptime(data[headers[0]][i], "%d/%m/%Y")

for index, (key, value) in enumerate(data.items()):
    if key == headers[0]:
        continue
    else:
        print(key)
        print(value)
        plt.plot(data[headers[0]], value, label = key)

plt.legend()
plt.show()