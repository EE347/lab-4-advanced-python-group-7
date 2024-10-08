import csv
import matplotlib.pyplot as plt
from datetime import datetime


plots = {}

with open('task9.csv', 'r') as file:        
    csvfile = csv.reader(file)
    headers = next(csvfile)

    data = {}

    for title in headers:
        print(title)
        data[title] = []

    for key, value in data.items():
        print(key)

    for row in csvfile:
        for index, title in enumerate(headers):
            data[title].append(row[index])

for i in range(len(data['Date'])):
    data['Date'][i] = datetime.strptime(data["Date"[i], "%d-%m-%Y"])

for index, (key, value) in enumerate(data.items()):
    if key == 'Date':
        continue
    else:
        plt.plot(value, data['Date'], label = key)

plt.legend()
plt.show()