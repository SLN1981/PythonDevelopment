a = "Hello world"
print(a)
print(a[0])  # First character
print(a[:5])  # First five characters
print(a[6:])  # Characters from index 6 to the end
print(len(a))  # Length of the string
print(a.lower())  # Convert to lowercase
print(a.upper())  # Convert to uppercase
a+= " Python "
print(a)  # Concatenate " Python" to the string
a=a*3 # 2  # Repeat the string
print(a)
print(a.find("world"))  # Find the index of "world"
b="String " \
"with \
multiple lines"
print(a.split())  # Split the string at ""

print("I'm going to inject %s text here, and %s text here." %('some','more')) # String formatting with % operator
x = "Hello"
y = "World"
print("Injecting this %s and this %s " %(x,y)) # String formatting with % operator
print("With %r you can format strings." %('Fred')) # String formatting with % operator using %r for representation

# Format using %d
print("The value of x is %d" %(10.8))  # Integer formatting
# Flota Format using %f
print("The value of x is %f" %(10.8))  # Float formatting
# Float Format using precision
print("The value of x is %.2f" %(10.876))  # Float formatting with 2 decimal places
# Format using format() method
print("My name is  {}".format("LN"))  # Using format() method
# Format using format multiple arguments
print("My family members names are {3} {2} {1} {0}".format("Nidhi","Hari","KK","LN"))
# Format using f-strings (Python 3.6+)
name = "LN"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Using f-strings for formatting
# Format using f-strings with floats
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")  # Using f-strings with float formatting