# 1.

class String:
    def getString(self, a):
        self.a = input()
    def printString(self, a):
        print(self.a.upper())

# 2.

class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
    
# 3.

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
# 4.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def show(self):
        print(f"coordinates: ({self.x}, {self.y})")
    def dist(self, d):
        return ((self.x - d.x) ** 2 + (self.y - d.y) ** 2) ** 0.5
    
# 5.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, s):
        if s > 0:
            self.balance += s
            print("пополнение успешно!")
        else:
            print("сумма пополнения должна быть положительна")
    def withdraw(self, s):
        if s > self.balance:
            print("недостаточно средств")
        else:
            self.balance -= s
            print("снятие успешно!")

# 6.

lst = [x for x in range(1, 20)]
print(list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), lst)))
