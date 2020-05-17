# -*- coding: utf-8 -*-

class Car( ):
    
    def __init__(self, color,year): #init function has two underscores both sides
        self.color = color
        self.year = year

#instantiating class objects
ford = Car("red", 2014)

print(ford.color, ford.year)


class Person():
    
    age = 34
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
name = input('Enter name: ')  
gender = input("Gender: ")

inno = Person(name, gender)

print(inno.name, inno.gender)