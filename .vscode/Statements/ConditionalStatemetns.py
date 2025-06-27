for i in range(1,10):
  if i % 2 == 0:
    print(f"{i} is divisible by 2")
  elif i % 3 == 0:
    print(f"{i} is divisible by 3")
  else:
    print(f"{i} is not divisible by 2 or 3")

def primeNumber(n):
  for i in range (2, n // 2):
    if n % i == 0:
      return False
  return True

n = int(input("Enter a number to check if it is prime: "))
if(primeNumber(n)):
  print(f"{n} is a prime number")
else:
  print(f"{n} is not a prime number")

   