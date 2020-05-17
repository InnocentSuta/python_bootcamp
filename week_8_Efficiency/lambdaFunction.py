
print((lambda x : x ** 2 )(4))

#this is the same as


def squared(x):

    return x ** 2

print(squared(4))

#passing multiple variables

print((lambda x,y : x * y) (5, 10)) # multiplies 5 by 10


# saving a lambda function into a variable

square = lambda x, y: x * y
result = square(10, 5)    # calls the lambda function stored in the square variable and returns 5 * 10
print(result)

#finding greater number using lambda

greater = lambda x, y : x if x > y else y
result = greater(15, 10)
print(result)