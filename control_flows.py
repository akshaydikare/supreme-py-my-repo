#https://docs.python.org/3/tutorial/controlflow.html
#if Statements
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Please enter a Positive number. Negative changed to zero')
elif x == 0:
    print('Zero : 0')
elif x == 1:
    print('Single : ONE')
else:
    print('More than Single')

#For Loop
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(f"Word is {w} and length is : ", len(w))

#Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(f"Original Collection : {users}")
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(f"Strategy:  Iterate over a copy : {users}")

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(f"Strategy:  Create a new collection {active_users}")

#The range() Function
for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])