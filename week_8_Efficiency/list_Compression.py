
#list compression

list_1 = [i for i in range(100)] # makes a list of numbers btn 1 to 100
print(list_1)

nums = [i for i in range(100) if i % 2 == 0]  # makes a list of even numbers between 0 to 100
print(nums)

list_2 = ["even" if i % 2 == 0 else "odd" for i in range(100)]
print(list_2)

squared = [num ** 2 for num in list_1]
print(squared)

#Dictionary compression
#creating a dictionary of even numbers and square values using comprehension

squares = { x: x **2  for x in list_1 if x % 2 == 0}
print(squares)

#Degree Conversion: Using list comprehension, convert the list below to Fahrenheit.
# Currently, the degrees are in Celsius temperatures. The conversion formula is "(9/5) * C + 32".
# Your output should be [53.6, 69.8, 59, 89.6].
#>>> degrees = [12, 21, 15, 32]

degrees = [12, 21, 15, 32]
fahrenheit  = [round((9/5 * f + 32)) for f in degrees]
print(fahrenheit)

num = int(input("Enter a number up to or including 100: "))
numberss = [x for x in range(1, 101) if x % num == 0]
print(numberss)
