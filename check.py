def check(price, name, *a,**b):
    
    #print(len(a))
    print(price, name)
    for i in a:
        print(i)

    for key in b.keys():
        print(b[key])
        
    return "Done"

sum = lambda a,b,c: a+b+c
print(sum(200,300,400))

def exponential_function(n):
  return lambda x : x ** n

square = exponential_function(2)
cube = exponential_function(3)





check(12, 'Jar','a',2,3,4,5,a=100,b=600,c=700,d=800)
print(square(16))
print(cube(4))
