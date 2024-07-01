# Creating a list, a dictionary, and a set

# List
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10
print("List after modifying an element:", my_list)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)

# Set
my_set = {1, 2, 3, 4, 5}
print("\nOriginal set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)


my_set.remove(2)
my_set.add(10)
print("Set after simulating modification:", my_set)
