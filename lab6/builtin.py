# 1

lst = [2, 4, 8, 3, 12, 17, 5]
multi = 1
for i in lst:
    multi *= i
print(multi)

# 2

string = input()
lw, up = 0, 0
for i in string:
    if i.islower():
        lw += 1
    if i.isupper():
        up += 1
print(f"Upper: {up}, lower: {lw}")

# 3

s = input()
ss = s[::-1]
if s == ss:
    print("yes")
else:
    print("no")

# 4

import time
r = float(input())
s = int(input())
time.sleep(s / 1000)
print(f"Square root of {r} after {s} miliseconds is {r ** 0.5}")

# 5

tup = (1, "fr", True)
if all(tup):
    print(True)
else:
    print(False)
