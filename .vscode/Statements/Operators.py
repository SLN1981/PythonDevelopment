from random import shuffle
from random import randint
my_list = list(range(1, 11))
for i in my_list:
    print(f"The number is {i} ")

my_alp_list = ['a', 'b', 'c', 'd', 'e']
my_word = "hello"
# splitting a string into a list of characters
my_char_list = list(my_word)
for i,j in enumerate(my_char_list):
    print(f"The {i+1}th letter is {j}")

my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
my_list3 = zip(my_list, my_list2)
for  i in my_list3:
    print(f"the elements are {i}")

print(f"Is my_list2 has 2 {2 in my_list2}")


print(min(my_list2))  # Minimum value in my_list2
print(max(my_list2))  # Maximum value in my_list2

shuffle(my_alp_list)  # Shuffle the list
print(f"Shuffled list: {my_alp_list}")

print(randint(1, 100))  # Generate a random integer between 1 and 100

name = input("Enter your name: ")
print(f"Hello, {name}!")