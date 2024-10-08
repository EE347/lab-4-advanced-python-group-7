import csv

with open('task5.csv', 'a') as file:
    # This is a CSV file, but it is not stated in the instructions to add commas after input values, only a new line, so assuming no commas.
    csvwriter =  csv.writer(file, delimiter='\n')
    while True:
        username = input("Give me your name, user: ")
        if username == "quit":
            break
        else:
            csvwriter.writerow([username])

print("Quitting...")