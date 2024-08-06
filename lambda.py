def myfunction(a,b):
    return a+b

print(myfunction(3,4))

my_lambda_function = lambda a,b: a+b

print(my_lambda_function(3,4))

def exponential(n):
    return lambda x: x**n

square = exponential(2)
mycube = exponential(3)

print(square(8))

print(mycube(16))



