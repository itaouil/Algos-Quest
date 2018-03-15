"""
    Given two strings, is one
    the permutation of the other.
"""

from collections import Counter

def is_permutation(str1, str2):

    # Check if lenghts differ
    if len(str1) != len(str2):
        return False

    # Build counter
    cnt = Counter(str1)

    # Check if permutation
    for char in str2:

        # Not a permutation
        if char not in cnt or cnt[char] == 0:
            return False

        else:
            cnt[char] -= 1

    return True

print(is_permutation("ilyass", "yassil"))
print(is_permutation("hello", "llohe"))
print(is_permutation("hello", "llohead"))
print(is_permutation("adas", "adds"))
