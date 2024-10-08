username = input("Give me your name, user: ")
with open("task3.txt", "a") as myfile:
    # Not clear if line breaks are required after each name, assuming they are required, due to task 4
    myfile.write(username + "\n")
print("Appended " + username + " to File!")