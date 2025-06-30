from random import randint
num_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(num):
    """Returns the square of a number."""
    return num * num    
squared_list =  list(map(square, num_List))
print(squared_list)  # Example usage
def  evn_numbers(num):
    """Returns True if the number is even, otherwise False."""
    return num % 2 == 0
even_list = list(filter(evn_numbers, num_List))
print(even_list)  # Example usage

even_square_list = list(filter(evn_numbers,map(square, num_List)))
print(even_square_list)  # Example usage

odd_filter = lambda num: num % 2 != 0

odd_cube_list =  list(filter(odd_filter, map(lambda num: num ** 3 ,num_List)))

print(odd_cube_list)  # Example usage

capitalize_first_fourth_letter = lambda name: name[0].upper() + name[1:3] + name[3].capitalize() + name[4:] if len(name) > 4 else name
print(capitalize_first_fourth_letter('macdonald'))  # Example usage

major_filter = lambda num: num > 18 

random_numbers = [randint(1, 100) for _ in range(10)]
print(random_numbers)  # Example usage
major_numbers = list(filter(major_filter, random_numbers))
print(major_numbers)  # Example usage
