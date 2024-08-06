lst=[["Joehan",(78,98,67,90,98)],
     ["Name2",(87,56,43,78,98)],
     ["Name3",(45,67,35,89,90)],
     ["Name4",(56,78,32,78,89)]]


pass_or_fail=input("Enter criteria(P/F) :")

if pass_or_fail =='P':
    for x in lst:
        for mark in x[1]:
            if mark>=45:
                all_pass=True
            else:
                all_pass=False
                break
        if all_pass == True:
            print(x)


if pass_or_fail =='F':
    for x in lst:
        fail=False

        for mark in x[1]:
            if mark<45:
                fail=True
                break
            
        if fail==True:
            print(x)
                
                    

            
            
