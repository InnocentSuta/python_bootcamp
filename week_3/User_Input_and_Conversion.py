# -*- coding: utf-8 -*-
#Accepting user input and Assigning it to a variable
name = input("Enter your name: ")
print(f"Hello {name}")

#checking for data type
print(type(name))

#converting to another data type

number = 5
print(type(number))

number = str(number)

print(type(number))

#converting user input and checking for errors

number = input("Enter a number to add: ")

try:
    result = 100 + int(number)
    print(f"100 + {number} = {result}")
except ValueError:
    print("Enter a number please")
     
    