# -*- coding: utf-8 -*-

list = [12, 11, 32, 2, 23, 1, 9, 0, 5, 560, 90, 34, 5, 7, 8]

#find length of the list

length = len(list)
print(length)

#slicing the list -- accessing specific items in the list

print(list[ 2 : 7])
print(list[  : 2])
print(list[3 : ])
print(list[-2: ])

#adding items to the list

list.append(222) #adds to the end of the list
print(list)

list.insert(4,342) #adds an item to the specific location or index
print(list)

#removing items in the list

list.pop(4) #removes the last element in the list or it can remove at specific loc
print(list)

list.remove(560) #removes the listed item
print(list)

print(sorted(list))


names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']

removed = []

for name in names:
    if name not in removed:
        removed.append(name)

print(removed)






