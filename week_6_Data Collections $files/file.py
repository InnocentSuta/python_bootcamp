# -*- coding: utf-8 -*-

# opening/creating and writing to a text file


f = open("test.txt", "w+") # open file in writing and reading mode
f.write("this is a test")
f.close( )

# reading from a text file
f = open("test.txt", "r")
data = f.read( )
f.close( )

print(data)

# opening/creating and writing to a csv file
import csv

with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow( ["Name", "City"] )
    writer.writerow( ["Craig Lou", "Taiwan"] )
    
    
# reading from csv files
with open("test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader: 
        print(row)
        