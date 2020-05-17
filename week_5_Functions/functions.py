# -*- coding: utf-8 -*-

#functions without parameters
def printInfo():
    print("Name: Innocent Suta")
    print("Age: 23")

printInfo()

def calc():
    x, y = 34, 45
    print(x * y)

calc()

#functions with parameters

def addNumbers(x, y, z):
    
    result = x + y + z
    
    print(f"sum: {result}")
    
addNumbers(3, 21, 45)

number = [12, 10, 67, 90, 65]

def squares(list):
    for i in list:
        print(f"Squared: {i **2}")

squares(number)

# setting default parameter values

def calcArea(r, pi = 3.14):
    
    area = pi * (r**2)
    print( f"Area: { area}" )
    
calcArea(2) # assuming radius is the value of 2

#Setting a parameter Optional

def printFullName(first, last, middle=""):
    if middle:
        print(f"Full Name: {first} {middle} {last}")
        
    else:
        print(f"Full Name: {first} {last}")

printFullName("Innocent", "Suta")

printFullName("Innocent", "Suta", "Adorat")


# using args parameter to take in a tuple of arbitrary values
def outputData(name, *args):
    print( type(args) )
    for arg in args:
        print(arg)
outputData("John Smith", 5, True, "Jess")

# using kwargs parameter to take in a dictionary of arbitrary values
def outputData(**kwargs):
    print( type(kwargs) )
    print( kwargs[ "name" ] )
    print( kwargs[ "num" ] )
outputData(name = "John Smith", num = 5, b = True)




#RETURN STATEMENTS FUNCTIONS

def multiply(x, y):
    
    return x * y

ans = multiply(70, 2)
print(ans)





















