#0,1,1,2,3,5,8,13,21,34,55,
#0,1,1,2



def Fibonacci(n):
    if n == 0:
        break
    elif n == 1:
        print(0)
    elif n == 2:
        print("0, 1")
    else:
        a, b = 0, 1
        print(a,",",b)
        #fib_series = [0, 1]
        for i in range(2, n):
            a, b = b, a + b
            print(",",b)
            #fib_series.append(b)
        #print(fib_series)
        
n = int(input("Enter how many numbers you want to generate in fibonacci: "))
Fibonacci(n)
