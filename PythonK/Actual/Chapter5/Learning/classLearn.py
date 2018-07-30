'''
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()

print(cal1.adder(3))


class Cookie:
    pass

Cookie()

class MoreCalculator(Calculator):
    def pow(self):
        result = self.result ** self.result
        return result

a = MoreCalculator()
a.adder(3)
print(a.pow())
'''

#Quiz 5
class Calculator:
    def __init__(self, list):
        self.list = list
        self.result = 0
    def sum(self):
        for x in self.list:
            self.result += x
        return self.result
    def mul(self):
        for x in self.list:
            self.result *= x
        return self.result

cal = Calculator([1, 2, 3, 4, 5])
print(cal.sum())
print(cal.mul())

