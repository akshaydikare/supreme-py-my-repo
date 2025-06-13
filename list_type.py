# Sequence Types: list
my_list = [1, 2, 'apple', 3.14]
print(f"\nType of {my_list}: {type(my_list)}")
print(f"Value: {my_list}")

for item in my_list:
    print(f"Item: {item}, Type: {type(item)}")
#================================================================================
my_list2 = [1, 2, 4, 5,6,7,8,9,10]

for item in my_list2:
    print(f"Item: {item} * 2 , Type: {item * 2}")  # This will print each item multiplied by 2}")
#================================================================================
list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"]

print("\nList of Months:")
for month in list_of_months:
    print(month)

#append a new month to the list, so we can use the method append of list.
list_of_months.append("December")  # Adding December to the list

print(f"Element Month at index 3 : {list_of_months[3]}")

print("\nList of Months:")
for month in list_of_months:
    print(month)

#================================================================================
# Create a list with repeated elements
# This snippet demonstrates how to create lists with repeated elements in Python.
# Create a list [2, 2, 2, 2, 2]
a = [2] * 5

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

print(a)
print(b)

#================================================================================
# Demonstrating list methods: append, insert, extend
# This snippet demonstrates how to use various list methods in Python.
# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)

#================================================================================
# Demonstrating list methods: remove, pop, and del
a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)