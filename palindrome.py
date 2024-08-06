str1="Money"
str2=""
length_=len(str1)
start_value = length_-1

#Reverse the given string
for i in range(start_value,-1,-1):
    str2=str2+str1[i]

print(str2)
if str1==str2:
    print("The given string is a palindrome")
else:
    print("The given string is NOT a palindrome")

