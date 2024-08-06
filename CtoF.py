#°F = (°C × 9/5) + 32

def CelciusToFaranheit(celcius):
    return celcius * (9/5)+32


celcius=float(input("Enter the temperature in celcius : "))

print(f"{celcius} degree Celcius is {CelciusToFaranheit(celcius)} degree Faranheit")
