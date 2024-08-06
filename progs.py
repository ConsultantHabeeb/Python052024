"""
use if ,if else ,nested if, while ,for -write a definition for each and write 2 programs under each -write on a paper and send it in WhatsApp or in LMS(total 3 page work -10 mark assignment )
"""


#Program 1

a=20
b=10
if a> b:
  print("a is greater")


a=True
if(a==True):
 print("a is TRUE")



a=10
b=20
if a> b:
  print("a is greater")
else:
  print("b is greater")


IsPriceKnown=True
if IsPriceKnown==True:
 print("The price is known")
else:
 print("The price is unknown")
 

a=70
b=20
c=30
if a>b:
 if a>c:
   print("a is greatest")


a=-1
b=-2
if a<0:
  if b<0:
    print("Both a and b are negative")
  else:
    print("a alone is negative")
else:
  if b<0:
   print("b alone is negative")


#print numbers from 1 to 5 using while
n=5
while n>0:
 print(n)
 n=n-1

#print numbers from 1 to 10 using while
count=10
while True:
  print("Count value is" , count)
  count=count-1
  if count<1:
   break;

#print numbers from 1 to 10 using for
for n in range(1,11):
 print(n)

#print even numbers between 2 and 100
for n in range(2,101,2):
 print(n)
