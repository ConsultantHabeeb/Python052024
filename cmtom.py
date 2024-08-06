def centimetertometer(cm):
    #100 cm = 1 m
    return cm/100


cm=float(input("Enter the cm : "))

print(f"{cm} centimeters is {centimetertometer(cm)} meters")
