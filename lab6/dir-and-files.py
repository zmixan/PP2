import os
# 1

p = input()
print("All")
for i in os.listdir(p):
    print(i)
print("Directories:")
for i in os.listdir(p):
    if os.path.isdir(os.path.join(p, i)):
        print(i)
print("Files:")
for i in os.listdir(p):
    if os.path.isfile(os.path.join(p, i)):
        print(i)

# 2

p = input()
print("Exists:", os.path.exists(p))
print("Readable:", os.access(p, os.R_OK))
print("Writable:", os.access(p, os.W_OK))
print("Executable:", os.access(p, os.X_OK))

# 3

p = input()
if os.path.exists(p):
    print("file exists")
    print("directory:", os.path.dirname(p))
    print("file name:", os.path.basename(p))
else:
    print("file does not exist")

# 4

with open("test.txt", "r") as f:
    sum = 0
    for _ in f:
        sum += 1
print(sum)

# 5

lst = [1, 2, 3]
with open("test.txt", "w") as f:
    for i in lst:
        f.write(str(i))

# 6

import string
for i in string.ascii_uppercase:
    with open(f"{i}.txt", "w") as f:
        f.write(f"This is {i} file")

# 7 

orig = input()
copy = input()
with open(orig, "r") as o:
    with open(copy, "w") as c:
        c.write(o.read())

# 8

delet = input()
if os.path.exists(delet) and os.access(delet, os.W_OK):
    os.remove(delet)
    print("deleted succesfully")
else:
    print("file doesn't exist or no permission to delete")
