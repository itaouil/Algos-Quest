"""
    Write a method to replace all spaces in
    a string with "%20". You may assume that
    the string has sufficient space at the end
    to hold the additional characters, and that
    you are given the "true" length of the string.

    Input: "Mr John Smith    "
    Outuput: "Mr%20John%20Smith"
"""

def urlify(string, length):

    # Cast string to list
    chars = list(string)

    # Get the number of spaces
    spaces = 0
    for x in range(length):
        if chars[x].isspace():
            spaces += 1

    # Space substitution
    start = length + spaces * 2

    for x in range(length-1, -1, -1):
        print(x + spaces * 2)
        if not chars[x].isspace():
            chars[x + spaces * 2] = chars[x]
        else:
            chars[x + spaces * 2] = '0'
            chars[x + spaces * 2 - 1] = '2'
            chars[x + spaces * 2 - 2] = '%'
            spaces -= 1

    return ''.join(chars)

print(urlify("Mr John Smith    ", 13))
