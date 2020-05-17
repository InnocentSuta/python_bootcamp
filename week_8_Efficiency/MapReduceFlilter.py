# using the map function without lambdas
def convertDeg(C):

    return (9/5) * C + 32

temps = [ 12.5, 13.6, 15, 9.2 ]

converted_temps = map(convertDeg, temps) # returns map object

print(converted_temps)

converted_temps = list(converted_temps) # type convert map object into list of converted temps

print(converted_temps)

# using a map function with lambdas

temps = [12.5, 13.6, 15, 9.2]
Fahrenheit = list(map(lambda c : (9/5) * c + 32, temps))
print(Fahrenheit)

# using the filter function without lambda functions, filter out temps below 55F

def filterTemps(C):
    converted = (9/5) * C + 32

    return True if converted > 55 else False # use ternary operator

temps = [ 12.5, 13.6, 15, 9.2 ]

filtered_temps = filter(filterTemps, temps) # returns filter object

print(filtered_temps)

filtered_temps = list(filtered_temps) # convert filter object to list of filtered data

print(filtered_temps)


# using the filter function with lambda functions, filter out temps below 55F

temps = [ 12.5, 13.6, 15, 9.2 ]

filtered_temps = list( filter( lambda C : True if (9/5) * C + 32 > 55 else False, temps) ) # type convert the filter

print(filtered_temps)

# for informational purposes this is how you use the reduce function
from functools import reduce

nums = [ 1, 2, 3, 4 ]

result = reduce( lambda a, b : a * b, nums ) # result is 24

print(result)