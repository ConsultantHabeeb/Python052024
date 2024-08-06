#Object oriented programming

class Bird:

    country='India'
    
    def __init__(self, color,height,weight):
            self.color=color
            self.height=height
            self.weight=weight

    def fly(self):
        print('I am flying')

    def eat(self):
        print('I am eating')

    def fight(self):
        print('I am fighting')



bird1 = Bird('Blue',15,100)
bird2 = Bird('Red',20,150)
bird3 = Bird('Green',30,200)


birds=[]
for i in range(1 to 10):
    bird=Bird('Blue',15,100)
    birds.append(bird)


    



bird1.weight =90

print(bird1.weight, bird1.height, bird1.color)
print(bird2.weight, bird2.height, bird2.color)
print(bird1.country)


bird1.fly()
