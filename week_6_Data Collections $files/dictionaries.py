# -*- coding: utf-8 -*-

#declaring dictionaries

empty = {} #empty data dictionary

person = {
    "name": "Innocent Suta",
    "age" : 23
    } #dictionary with values

print(person)

#accessing data from a dictionaries

print(person["name"])

ag = person.get("age", "Age not available") # better way to retrieve data using get method
print(ag)

#dictionary with lists

data = {"sports":["baseball", "football","cricket","basketball"]}

print(data)

print(data["sports"][2])

#list with dictionary

info = ["jon", "james", {"name": "Innocent","age":23}]

print(info[2]["age"])


#dictionary with dictionary

datas = {
    "Team": "Chelsea FC",
    "wins" : {"2018": 107, "2019": 219}
    }


print(datas["wins"])
print(datas["wins"]["2019"])


#working with dictionary 
#adding new information

car = { "name": "audi"}

#adding year and color to the car dictionary

car["year"] =  2018

car["color"] = "blue" 

print(car)

#changing information

car["year"] = 2006  #changed the year to 2006

print(car)

#deleting dictionary pair using del 


try:
    del car["year"]
    print(car)
    
except:
    
    print("don't exist")

#looping a dictionary
    
#looping using only keys

persons = {
    "name": "Innocent Suta",
    "age": 24,
    "course":"Bsc Computer Science"}
    

for key in persons.keys():
    print(key) #prints only the key e.g name
    print(persons[key]) #prints the value at that key.
    
#looping using only values
    
for value in persons.values():
    print(value)

#looping using both key and values
    
    for key, value in persons.items():
        print(f"{key} : {value}")
        
        
        
#exercise accept user input and output it.
        
student = {}

studentNumber = input("Enter Student #: ")

student["StudentNumber"] = studentNumber

for key in student.keys():
    print(f"{key} : {student[key]}")



    
    
    
    
    
    
    
    
    
    
    
    