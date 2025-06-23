new_dict={"Key1":"Value1","Key2":"Value2","Key3":"Value3"}
print(new_dict) # Print the dictionary
print(new_dict["Key1"])  # Access value by key
fruit_prices={"Apple": 1.2, "Banana": 0.5, "Cherry": 2.0}
print(fruit_prices)  # Print the dictionary of fruit prices
fruit_prices["Banana"] *=2  # Update the price of Banana
print(fruit_prices)  # Print the updated dictionary
animal_dict = {}
animal_dict["Dog"] = "Bark"  # Add a new key-value pair
print(animal_dict)  # Print the dictionary with the new key-value pair
nested_dict = {
    "Fruits": {
        "Apple": 1.2,
        "Banana": 0.5,
        "Cherry": 2.0
    },
    "Vegetables": {
        "Carrot": 0.8,
        "Broccoli": 1.5,
        "Spinach": 1.0
    }
}
print(nested_dict)  # Print the nested dictionary
print(nested_dict["Fruits"]["Apple"])  # Access a value in the nested dictionary
print(nested_dict.keys())
print(nested_dict.values())  # Print all values in the dictionary
print(nested_dict.items())  # Print all key-value pairs in the dictionary
nested_dict["Groceries"] = {
    "Rice": 2.0,
    "Pasta": 1.5,
    "Bread": 1.0
}
# Add a new key-value pair to the nested dictionary
print(nested_dict)  # Print the updated nested dictionary