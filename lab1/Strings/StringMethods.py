# capitalize()	Converts the first character to upper case
print("hello".capitalize())  # "Hello"
# casefold()	Converts string into lower case
print("HELLO".casefold())  # "hello"
# center()	Returns a centered string
print("hello".center(10, "*"))  # "**hello***"
# count()	Returns the number of times a specified value occurs in a string
print("hello world".count("o"))  # 2
# encode()	Returns an encoded version of the string
print("hello".encode())  # b'hello'
# endswith()	Returns true if the string ends with the specified value
print("hello".endswith("o"))  # True
# expandtabs()	Sets the tab size of the string
print("hello\tworld".expandtabs(4))  # "hello   world"
# find()	Searches the string for a specified value and returns the position of where it was found
print("hello world".find("o"))  # 4
# format()	Formats specified values in a string
print("Hello, {}!".format("world"))  # "Hello, world!"
# format_map()	Formats specified values in a string
print("Hello, {name}!".format_map({"name": "world"}))  # "Hello, world!"
# index()	Searches the string for a specified value and returns the position of where it was found
print("hello world".index("o"))  # 4
# isalnum()	Returns True if all characters in the string are alphanumeric
print("hello123".isalnum())  # True
# isalpha()	Returns True if all characters in the string are in the alphabet
print("hello".isalpha())  # True
# isascii()	Returns True if all characters in the string are ascii characters
print("hello".isascii())  # True
# isdecimal()	Returns True if all characters in the string are decimals
print("12345".isdecimal())  # True
# isdigit()	Returns True if all characters in the string are digits
print("12345".isdigit())  # True
# isidentifier()	Returns True if the string is an identifier
print("hello".isidentifier())  # True
# islower()	Returns True if all characters in the string are lower case
print("hello".islower())  # True
# isnumeric()	Returns True if all characters in the string are numeric
print("12345".isnumeric())  # True
# isprintable()	Returns True if all characters in the string are printable
print("hello".isprintable())  # True
# isspace()	Returns True if all characters in the string are whitespaces
print("   ".isspace())  # True
# istitle() 	Returns True if the string follows the rules of a title
print("Hello World".istitle())  # True
# isupper()	Returns True if all characters in the string are upper case
print("HELLO".isupper())  # True
# join()	Joins the elements of an iterable to the end of the string
print("-".join(["a", "b", "c"]))  # "a-b-c"
# ljust()	Returns a left justified version of the string
print("hello".ljust(10, "*"))  # "hello*****"
# lower()	Converts a string into lower case
print("HELLO".lower())  # "hello"
# lstrip()	Returns a left trim version of the string
print("   hello".lstrip())  # "hello"
# maketrans()	Returns a translation table to be used in translations
print(str.maketrans("abc", "123"))
# translate()	Returns a translated string
print("abc".translate(str.maketrans("abc", "123")))  # "123"
# partition()	Returns a tuple where the string is parted into three parts
print("hello world".partition(" "))  # ("hello", " ", "world")
# replace()	Returns a string where a specified value is replaced with a specified value
print("hello world".replace("world", "Python"))  # "hello Python"
# rfind()	Searches the string for a specified value and returns the last position of where it was found
print("hello world".rfind("o"))  # 7
# rindex()	Searches the string for a specified value and returns the last position of where it was found
print("hello world".rindex("o"))  # 7
# rjust()	Returns a right justified version of the string
print("hello".rjust(10, "*"))  # "*****hello"
# rpartition()	Returns a tuple where the string is parted into three parts
print("hello world".rpartition(" "))  # ("hello", " ", "world")
# rsplit()	Splits the string at the specified separator, and returns a list
print("hello world python".rsplit(" ", 1))  # ['hello world', 'python']
# rstrip()	Returns a right trim version of the string
print("hello   ".rstrip())  # "hello"
# split()	Splits the string at the specified separator, and returns a list
print("hello world python".split(" "))  # ['hello', 'world', 'python']
# splitlines()	Splits the string at line breaks and returns a list
print("hello\nworld\npython".splitlines())  # ['hello', 'world', 'python']
# startswith()	Returns true if the string starts with the specified value
print("hello".startswith("h"))  # True
# strip()	Returns a trimmed version of the string
print("   hello   ".strip())  # "hello"
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("Hello World".swapcase())  # "hELLO wORLD"
# title()	Converts the first character of each word to upper case
print("hello world".title())  # "Hello World"
# upper()	Converts a string into upper case
print("hello".upper())  # "HELLO"
# zfill()	Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5))  # "00042"
