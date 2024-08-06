class Item:
    brand=""
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name}'s price is {self.price} per kg"

    def GetPriceForQuantity(self,n):
        return(n*self.price)

    def SetBrand(myitem,brand):
        myitem.brand=brand
        
    def GetBrand(myitem):
        return(myitem.brand)

item = Item("Rice",90)

print(item.GetPriceForQuantity(20))

print(item)
        
    
