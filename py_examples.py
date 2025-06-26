# compound interest for given values.

def compound_interest(principal, rate, time):

    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Calling the function with example values
# principal = 10000, rate = 10.25%, time = 5 years
compound_interest(1000000, 13.25, 5)

#===============================================================================================
s = "FAKE To TAKE"

# Split the string into words, reverse the list of words, and join them back
reversed_words = ' '.join(s.split()[::-1])

print(reversed_words) #TAKE To FAKE

"""Explanation:

The split() method splits the string into a list of words.
[::-1] reverses the list of words.
join() combines the reversed words back into a single string."""

#===============================================================================================

from collections import Counter

# Input string
s = "hello world hello everyone - hello world hello everyone"

# Calculate word frequencies using Counter
w_freq = Counter(s.split())

print(w_freq)