di={"key1":"value1","key2":"value2",
    "key3":"value3","key4":"value4"}

d2={"AbdulWahid":[96,89,90,68,98]}
d3={"AbdulWahid":(96,89,90,68,98)}

myname="Hamdan"

for key, value in di.items():
    print(f"Hi {myname}, The key is {key}, and the value is {value}")


for value in di.values():
    print(value)


for k in di.keys():
    print(k)
