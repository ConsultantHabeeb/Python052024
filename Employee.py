class Employee:
    def __init__(self,n,a,q):
        self.name=n
        self.age=a
        self.qualification = q

    def getDetails(self):
        print("You are {0}, {1} years old, studied {2}"
              .format(self.name,
                      self.age,
                      self.qualification))

    def setDetails(self, n, a, q):
        """Set the details
                of the object"""
        self.name=n
        self.age=a
        self.qualification=q

class Manager(Employee):
    def __init__(self,n,a,q):
        super().__init__(n,a,q)


    def getDetails(self):
        print("You are a Manager. Your name is {0}, {1} years old,studied {2}"
              .format(self.name,
                      self.age,
                      self.qualification))

