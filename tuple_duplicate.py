t1=(1,12,2,2,2,3,11,3,4,4,5,6,7,8,9,9,9,10,11,9,12,10,11)
list=[1,2,3,4,5]

#(1,2,3,4,5,6,7,8,9)

tuple_temp=()

#tuple_temp = (tuple_temp,100)

print('The given tuple is',t1)
#t1=(1,12,2,2,2,3,11,3,4,4,5,6,7,8,9,9,9,10,11,9,12,10,11)

for x in t1:
    for y in t1:
        if x!=y:
          if x not in tuple_temp:
            tuple_temp=tuple_temp +(x,)
            break

print(tuple_temp)
