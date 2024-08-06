

#This program is to find if the given number is odd or even

a=int(input("Enter number to check"))

#% is called mod - gives the reminder
result=a%2



match result:
    case 0:
            print("It is even")

    case 1:
            print("It is odd")
    case _:
            print("Defalut")

