"""
Positional
Optional
Named
Multiple
Disctionary
"""
def multiple_args(*args):
    for arg in args:
        print(arg)

multiple_args(1,2,3,4,5)

def display(**values):
    for key in values.keys():
        print(key)


display(a=2,b=3,c=4,d=5)

display(Rice="12",Wheat="20")

