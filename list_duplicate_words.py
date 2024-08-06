#Find out the duplicates between two lists
list1 =["aaa","bbb","ccc","ddd","new"]
list2 =["aaa","bbb1","ccc","ddd1","new"]

list_common=[]

for l1_word in list1:
    for l2_word in list2: 
        if l1_word == l2_word:
            list_common.append(l1_word)
            break
    #more statements

print(list_common)   




