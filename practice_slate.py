#https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

#The keyword argument "end" can be used to avoid the newline after the output, or end the output with a different string:

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

#other payload of print
i = 256*256
print('\n\nThe value of i is', i)
#======================
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('\nLetters: ', letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print('\nLetters after adding new letters at 2:5: ', letters)

# now remove them
letters[2:5] = []
print('\nLetters after removing new letters at 2:5: ', letters)


# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

#===================================================>>
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object

rgba.append("Alph")
print(rgb)

#==================================================>>
tax = 12.5 / 100
price = 100.50
print(round(price + (price * tax), 2))

#===============================
5 ** 2  # 5 squared = 25
2 ** 7  # 2 to the power of 7 = 128

#===============================


