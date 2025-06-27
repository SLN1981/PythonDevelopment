x = 0 
j = 0;
while x < 10:
    print("I am the square of", x, ":", x**2)
    j += x**2
    x += 1
else: 
    print("The sum of squares from 1 to 9 is", j)

# example of continue statement in while loop
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:  # Skip even numbers
        continue
    print("I am the odd number", x)
# example of break statement in while loop
x = 0       
while x < 10:
    x += 1
    if x == 9:  # Break the loop when x is 5
        break
    print("I am the number", x)
# while with pass example
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:  # Skip even numbers
        pass  # Do nothing for even numbers
    else:
        print("I am the odd number", x)

word = "My name is John"
list = list(word)
for i in list :
   print(i)

for i,j in enumerate(list):
    print(i, j)     