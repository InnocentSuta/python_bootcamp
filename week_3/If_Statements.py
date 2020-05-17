# -*- coding: utf-8 -*-

x , y = 5 , 29

if x < y :
    
    print(f"{x} is less than {y}")


#logical operators
    
# using the keyword 'and' in an 'if statement'
    
x, y, z = 5, 10, 5

if x < y and x == z:
    print("Both statements were true")
    
    
# using the keyword 'or' in an 'if statement'
x, y, z = 5, 10, 5

if x < y or x != z:
    print("One or both statements were true")

#membership operators
# using the keyword 'in' within an 'if statement'
    
name = "Innocent Suta"

if "n" in name:
    print(f"{name} contains character n")

if"i" not in name: #small letter
     print(f"{name} doesn't contain character i")
     
     
#Checking Inclusion – Part 1: Ask the user for input, and check to see if what
#they wrote includes an “es”.

word = input("Enter a word: ")

if 'es' in word:
    print(f"{word} contains 'es'")
else:
    print(f"{word} doesn't have 'es'")
     
     
#elif

num = int(input("Enter a number: "))

if num > 100:
    
    print("f{num} is Greater than 100")
    
elif num < 100:
    
    print(f"{num} is less than 100")
     
     
     
     
# writing a full conditional statement with if, elif, else
    
name = input("Enter a name: ")

if name[0] == "A":
    
    print("Name starts with an A")
    
elif name[0] == "B":
    
    print("Name starts with a B")
    
elif name[0] == "J":
    
    print("Name starts with a J")

else: # covers all other possibilities
    print( f"Name starts with { name[0] }")
     
     
     
     
     
     
