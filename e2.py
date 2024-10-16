import csv

with open('files/temperature.csv','r') as file:
    data=list(csv.reader(file))

city=input("enter station: ")

for i in data[1:]:
    if i[0]== city:
        print(i[1])
print(data)