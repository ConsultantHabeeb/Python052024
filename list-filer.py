lst=["para1 word this is to test aksdjfhks  asdjkhk sadjh",
     "para2 word this is to test",
     "para3 word1 this is to test",
     "para4 word this is to test ASJHD JASDNHJ ",
     "para5 word1 this is to test",
     "para6 word1 this is to test"]

search_word="word1"

lst2=[]

for x in lst:
    if search_word in x:
        lst2.append(x)

print(lst2)
        
        
        
