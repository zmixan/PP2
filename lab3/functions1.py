# 1.

a = float(input("Enter the number of grams: "))
print(f"{a} grams in ounces is {28.3495231 * a}")

# 2.

a = float(input("Enter the temperature in Fahrenheit: "))
print(f"{a} F is {(5 / 9) * (a - 32)} C")

# 3.

def solve(numheads, numlegs):
    y = (numlegs / 2) - numheads
    x = (numlegs / 2) - (2 * y)
    return x, y

# 4.

def isprime(a):
    if a % 2 == 0 or a == 1:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
def filter_prime(a):
    for i in a:
        if isprime(i):
            print(i, end = " ")

# 5.

import itertools
a = input()
b = itertools.permutations(a)
for c in b:
    print("".join(c))

# 6.

a = input().split()
for i in range(len(a) - 1, -1, -1):
    print(a[i], end = " ")

# 7.

def has33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# 8. 

def spy_game(a):
    v = False
    b = False
    c = False
    i1 = 0
    i2 = 0
    for i in range(len(a)):
        if i == 0:
            v = True
            i1 = i
            break
    if v:
        for i in range(i1, len(a)):
            if i == 0:
                b = True
                i2 = i
                break
    if v and b:
        for i in range(i2, len(a)):
            if i == 7:
                b = True
                break

# 9.

import math
def VofSphere(r):
    return ((4 / 3) * math.pi * r ** 3)

# 10.

def UniItems(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

# 11.

def ispalindrome(a):
    return a == a[::-1]

# 12.

def histogram(a):
    for i in a:
        print("*" * i)

# 13.

import random
a = input("Hello! What is your name? \n")
print(f"Well, {a}, I am thinking of a number between 1 and 20.")
b = random.randint(1, 20)
i = 0
while True:
    i += 1
    c = int(input("Take a guess.\n"))
    print()
    if c == b:
        print(f"Good job, {a}! You guessed my number in {i} guesses!")
        break
    elif c < b:
        print("Your guess is too low.")
        continue
    elif c > b:
        print("Your guess is too high.")
        continue