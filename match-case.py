#match case, while, boolean, tuple, complex


my_variable = input("Enter the option: ")
match my_variable:
    case 'A':
        print('The value is A')
    case 'B':
        print('The value is B')
    case 'C':
        print('The value is C')
    case 'D':
        print('The value is D')
    case _:
        print('Not matching')


#while Condition:
#    Statements

a=10
my_variable = True
while my_variable:
    print(a)
    a=a-1
    if a==0: my_variable = False


lst=[1,2,3,4,5]
lst.append(60)
print(lst)
t1=(1,2,3,4,5,6,"Test",45.5)
print(t1)


c=10+12j
print(c)

        
