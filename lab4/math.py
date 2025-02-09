import math

# 1

print("Output radian:", math.radians(float(input("Input degree: "))))

# 2

print("Expected Output:", float(input("Height: ")) * (float(input("Base, first value: ")) + float(input("Base, second value: "))) / 2)

# 3

n = int(input("Input number of sides: "))
x = float(input("Input the length of a side: "))
print("The area of the polygon is:", (x ** 2 * n) / (4 * math.tan(math.pi / n)))

# 4

print("Expected Output:", float(input("Length of base: ")) * float(input("Height of parallelogram: ")))