def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2  

print(add(5, 3))  # Example usage

def myfunc(boolVal):
 if boolVal:
  print('Hello')
 else:
  print('Goodbye')


def old_macdonald(name):
  if len(name) > 4:
   my_list =name[0].upper()+name[1:3]+name[3].capitalize()+name[4:]
   print(''.join(my_list))


old_macdonald('macdonald')

def master_yoda(text):
    """Reverses the order of words in a given text."""
    return ' '.join(text.split()[::-1])


# Distinct characters in a string in sorting order
def distinct_characters(text):
print(set('Mississippi'))

  