# -*- coding: utf-8 -*-

#loops using range
for num in range(10, 20):
    print(num)

#looping through items

list = [2, 32, 12]

for i in list:
    print(i)

name = "Suta"

for l in name:
    print(l)

print("\n")
lists = [1, 4, 12, 3, 5, 32]    

for i in lists:
    if i == 3:
        continue
    print(i)

print("\n")
for i in lists:
    if i == 3:
        break
    print(i)

print("\n")
for i in lists:
    if i == 3:
        pass
    print(i)


user = input("Enter a string: ")

for v in user:
    if v == "a":
        print(v)
    elif v == "e":
        print(v)
    elif v == "i":
        print(v)
    elif v == "o":
        print(v)
    elif v == "u":
        print(v)


