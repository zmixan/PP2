import re

with open("row.txt", "r") as f:
    s = f
# 1

if re.search("ab*?", s):
    print("Found a match!")
else:
    print("Not matched")

# 2

if re.search("ab{2, 3}?", s):
    print("Found a match!")
else:
    print("Not matched")

# 3

if re.search("[a-z]+?_[a-z]+?", s):
    print("Found a match!")
else:
    print("Not matched")

# 4

if re.search("[A-Z][a-z]+?", s):
    print("Found a match!")
else:
    print("Not matched")

# 5

if re.search("a.*b$", s):
    print("Found a match!")
else:
    print("Not matched")

# 6

re.sub("[\s,.]", ":", s)
print(s)

# 7
lst = re.findall("([^_]+)", s)
c = "".join([x.capitalize() for x in lst])
print(c)

# 8

print(re.findall("([a-zA-Z][^A-Z]*)", s))

# 9

s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
print(s)

# 10

lst = re.findall("([A-Z][]a-z0-9]+)", s)
c = "_".join([x.lower() for x in lst])
print(c)
