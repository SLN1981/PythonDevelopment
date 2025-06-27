list = [x for x in 'hello']
print(list)
square_list = [(x // 2) **2 for x in range(1,10)]
print("I am the square list", square_list)
evem_list = [x for x in range(1,10) if x % 2 == 0]
print("I am the even list", evem_list)
cube_three_divisible_list = [x ** 3 for x in range(1, 10) if x % 3 == 0]
print("I am the cube of numbers divisible by 3", cube_three_divisible_list)
     