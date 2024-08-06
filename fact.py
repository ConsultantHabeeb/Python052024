
def Factorial(n):
    if n==0 or n==1: return 1

    result=1
    
    while n>1:
        result = result * n
        n=n-1

    return result

#n!             = n * (n-1)!

#n!  =n * Fact(n-1)

#5!   5*4*3*2*1 = 5 * (5-1)!
#4!   4*3*2*1   = 4 * (4-1)!
#3!   3*2*1
#2!   2*1

#Recursion
#Recursive Function
def FactorialNested(n):
    if n==1: return 1
    return n * FactorialNested(n-1)


    
#Factorial Number

#Fact of 3 = 3 * (3-1) * (3-2)
#Fact of n = n * (n-1) * (n-2) *.... *(n-(n-1)
#Fact of n = n * (n-1) * (n-2) *.... *1

n=int(input("Enter the n value: "))

print("From Normal Function:", Factorial(n))

#Recursive Function
print("From Recursive Function:", FactorialNested(n))
