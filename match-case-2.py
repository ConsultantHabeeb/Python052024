

#This program is to demo match-case

a=input("Enter your option")

match a:
    case "Add":
            print("It is Addition")
    case "Sub":
            print("It is Subtraction")
    case "Mul":
            print("It is Multiplication")
    case "Div":
            print("It is Division")
    case _:
            print("Defalut")

