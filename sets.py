my_list =[10,25,46,56,20,46,56,25]
my_set= set(my_list)
print(f"Original List: {my_list}")
print(f"Set from List: {my_set}")
# Demonstrating set operations
# This snippet demonstrates how to create a set from a list and perform set operations in Python.

my_set2 = {10, 25, 46, 56, 20, 46, 56, 25}
print(f"Set 2: {my_set2}")

# Check if two sets are equal
print(f"Are the sets equal? {my_set == my_set2}")  
# Check if an element is in the set
print(f"Is 10 in my_set? {10 in my_set}")
# Check if an element is not in the set
print(f"Is 100 not in my_set? {100 not in my_set}")

my_set2.add(100)  # Adding an element to the set
print(f"Set 2 after adding 100: {my_set2}")

# Remove an element from the set
my_set2.remove(100)  # Removing an element from the set
print(f"Set 2 after removing 100: {my_set2}")

my_set2.pop()
# Remove and return an arbitrary element from the set
print(f"Set 2 after popping an element: {my_set2}")

x = my_set2.copy()
print(x)

clear_set = my_set2.clear()
print(f"Set 2 after clearing: {my_set2}")

#================================================================================
# Demonstrating set operations with union, intersection, and difference     
# This snippet demonstrates how to perform union, intersection, and difference operations on sets in Python.
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8}
# Union of two sets
# This will create a new set containing all elements from both sets
set_union = set_a.union(set_b)
print(f"Union of set_a and set_b: {set_union}")     
# Intersection of two sets
set_intersection = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b: {set_intersection}")
# Difference of two sets
set_difference = set_a.difference(set_b)    
print(f"Difference of set_a and set_b: {set_difference}")        


