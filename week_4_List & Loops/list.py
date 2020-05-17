# -*- coding: utf-8 -*-

#declaring a list

list = [3, 4.5, 12, 1, 2] 
print(list)

print(list[2])

num = list[1]

print(num)

#list with different data types

data = [23, "Innocent", True]

print(data)

#list within the list

info = [["innocent", "John", "Thomas"], [23, 34, 19], 2]
print(info)
print(info[2])

#accessing the list within the list

print(info[1][2])

#coping the list using [:] or using methdy .copy()

data_Copy = data[ : ]
print(data_Copy)

info_copy = info.copy()
print(info_copy)


names = ["John", "Abraham", "Sam", "Kelly"]

print(names[0][0],names[1][0],names[2][0],names[3][0])


sports = [["I like to play "],["soccer", "ruby", "netball", "basketball"]]

print(sports[0], sports[1][0])






