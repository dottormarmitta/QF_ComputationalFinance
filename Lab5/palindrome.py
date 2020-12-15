# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: functions
# #

# My task-performing method:
# my approach is to revert the given string O(n)
# and then check whether is equal or not to the given one
#
# @param s, a string
# @return bool
def isPalindrome(s):
    return (revertString(s) == s)

def revertString(s):
    outputString = ""
    i = len(s)-1
    while (i >= 0):
        outputString += s[i]
        i -= 1
    return outputString

# #
# Part 2: some testing
# #
s = "aaabbaaa"
print(isPalindrome(s))
