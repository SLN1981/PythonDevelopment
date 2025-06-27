my_list =[1, 2, 3, 4, 5]
for i in my_list:
    print("I am the square list", i**2)
fruit_price = {'apple': 2, 'banana': 1, 'orange': 3}
for k,v in fruit_price.items():
    print(f"The price of {k} is {v} rupees.")
tuple = (1, 2, 3, 4, 5)
for i in tuple:
    print("I am the scubequare tuple", i**3)
my_string = "Hello"
for char in my_string:
    print(f"I am the {char} who is the   {my_string.index(char)+1}th character  in the word {my_string}") 

j = 0
for i in range(1, 10):
    j += i
print(f"The sum of numbers from 1 to 10 is {j}") 

# Tuple unpacking in for loop
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Coordinate: ({x}, {y})")
my_three_tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)] 
for a, b, c in my_three_tuple_list:
    print(a,b,c)