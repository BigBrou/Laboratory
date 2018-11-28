class FirstClassInPython:
  color = 'Red'
  TupleInClass = ()
  def taste(self):
      return 'Delicious'

Class1 = FirstClassInPython()
print(Class1.color)
print(Class1.taste())

Class1.color = 'Green'
print(Class1.color)

VariousColor = ['Red', 'Green', 'Blue']
Class1.color = VariousColor[2]
print(Class1.color)

TupleOfColor = ('NewOne', 'Gray')
TupleOfColor = 'DarkGray'
print(TupleOfColor)

Class1.TupleInClass = TupleOfColor
print(Class1.TupleInClass)

class Stuff:
    bouns = 3000;
    def Salary(self):
        return self.bouns + 10000

AStuff = Stuff()
print(AStuff.Salary())


class joker:
    def __init__(self, bonus):
        self.bonus = bonus
    def Salary(self):
        salary = 100000 + self.bonus
        return salary

batman = joker(1000)
print(batman.Salary())
