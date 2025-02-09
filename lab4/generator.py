# 1

def square_generator(n):
    for i in range(n):
        yield i ** 2

# 2

def comma_even(n):
    for i in range(0, n + 1, 2):
        yield i
l = comma_even(int(input()))
for i in l:
    print(i, end=", ")

# 3

def div3and4(n):
    for i in range(0, n + 1, 12):
        yield i
for i in div3and4(int(input())):
    print(i, end=" ")

# 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
for i in squares(int(input()), int(input())):
    print(i, end = " ")

# 5

def down(n):
    for i in range(n, -1, -1):
        yield i
