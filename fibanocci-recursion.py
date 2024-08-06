def Fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        FibonacciSeries = Fibonacci(n-1)
        FibonacciSeries.append(FibonacciSeries[-1] + FibonacciSeries[-2])
        return FibonacciSeries


print('Enter the numbers for fib series')
n=int(input())

print(f" The Fibonacci series up to {n} numbers is: {Fibonacci(n)}")
