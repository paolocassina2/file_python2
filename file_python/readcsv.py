import csv
with open("C:\\Users\\Attilio\\Desktop\\ciao1.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
