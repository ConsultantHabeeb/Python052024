def Fibanocci(a,b,n,lst):
    if n==2: return
    
    lst.append(a+b)
    a,b=b,a+b
    Fibanocci(a,b,n-1,lst)
    


print('Enter the numbers for fib series')
n=int(input())
if n==1:
        print('0')
if n==2:
        print('0,1')
elif n>2:
        lst=[]
        Fibanocci(0,1,n, lst)
        lst = [0,1]+lst
        
        print(lst)
        
   
    
