"""
    Is the string made
    up of only unique
    characters.

    Assumptions:
        - String is in ASCII format
        - ASCII made of 128 chars (possibly 256 if extended)
"""

def isUnique(string):

    # Check if array exceeds
    # number of characters. In
    # that case just return False
    if len(string) > 128:
        return False

    # Array of booleans
    bool_array = [False for x in range(128)]

    # Check if unique
    for x, char in enumerate(string):

        # ASCII position
        ascii_index = ord(char)

        # Not unique
        if bool_array[ascii_index]:
            return False

        else:
            bool_array[ascii_index] = True

    return True

print(isUnique("uniqe"))
print(isUnique("ilyass"))
print(isUnique("bloomberg"))
print(isUnique("google"))
