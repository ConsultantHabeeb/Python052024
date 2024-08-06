class Person:
  school = "Avichi"
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.school="IISJ"
p1.myfunc()

print(p1.school)

