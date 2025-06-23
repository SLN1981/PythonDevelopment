myList = [1,2,3,4,5]
myMixedList = [1, "Hello", 3.14, True]
print(len(myList))  # Length of the list
print(myList[0])  # First element
print(myList[1:])  # Last element
print(myList[:3])  # Last element using negative indexing
newList = myList + [6, 7, 8]  # Concatenate lists
print(newList)  # Print the new list
newList[0] = 10  # Modify the first element
print(newList)  # Print the modified list
newList.append(9)  # Append an element to the list
print(newList)  # Print the list after appending
newList.remove(2)  # Remove an element from the list
print(newList)  # Print the list after removing an element
pop =newList.pop()  # Remove the last element from the list
print("Popped element:", pop)  # Print the popped element
print(newList)  # Print the list after popping the last element
newList.reverse()
print(newList)
newList.sort()  # Sort the list in ascending order
print(newList)  # Print the sorted list

#Nested Lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
nested_list = [list_1, list_2, list_3]  # Create a nested list
print(nested_list)  # Print the nested list
print(nested_list[0])  # Access the first sublist
print(nested_list[1][2])  # Access the third element of the second sub