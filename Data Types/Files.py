
myFile = open('test.txt')
print(myFile.read())

myFile.seek(0)  # Reset the file pointer to the beginning
print(myFile.read())
myFile.seek(0)
myFile.close()  # Close the file

with open('test.txt', 'r') as myFile:
    print(myFile.read())  # Read the file content

with open('test.txt', 'w') as myFile:
    myFile.write("Hello, World!")  # Write to the file

with open('test.txt', 'r') as myFile:
    content = myFile.read()  # Read the file content
    print(content)  # Print the content of the file

# Appending to a file
with open('test.txt', 'a') as myFile:
    myFile.write("\nAppending new line.")  # Append a new line to the file

with open('test.txt', 'r') as myFile:
    content = myFile.read()  # Read the file content
    print(content)  # Print the content of the file after appending