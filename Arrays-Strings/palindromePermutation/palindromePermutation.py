# -*- coding: utf-8 -*-

"""
    Given a string, write a function to check if it is a permutation of a palindrome (if by permuting the string we can obtain a palindrome). A palindrome is a word or phrase that is the same forward and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    Input: Tact Coa
    Outuput: True (“taco cat”, “atco cta”, etc.)
"""

# ASCII values for a and z
A = ord('a')
Z = ord('z')

# Find number of odd
# recurrences
def getMaxOdds(array):

    max_odds = 0

    for count in array:
        if count % 2:
            max_odds += 1

    return max_odds

def palindromePermutation(string):

    # Chars array
    chars = [0 for x in range(26)]

    # convert string to lowercase
    string = string.lower()

    # Populate chars occurences
    for char in string:

        # Get ASCII value
        val = ord(char)

        if A <= val and val <= Z:
            chars[val - A] += 1

    # Get max odd occurences
    max_odds = getMaxOdds(chars)
    print(max_odds)

    return True if max_odds < 2 else False

print(palindromePermutation("ilyass"))
print(palindromePermutation("Taco cat"))
