def find_even(given_list):
    temp_list=[]
    for i in given_list:
        if i%2 == 0:
            temp_list.append(i)

    return temp_list
        

n=int(input("Enter the number of items in your list"))

my_list=[]
for i in range(1,n+1):
      temp=int(input(f"Enter the number {i}"))
      my_list.append(temp)
      

print(f"The given list is\n{my_list}")

result_list= find_even(my_list)

print(f"The result list is \n {result_list}")


