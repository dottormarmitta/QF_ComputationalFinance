# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

import time

# #
# Part 1: functions
# #

# My task-performing method:
# my approach is to revert the given string
# and then check whether is equal or not to the given one
# This is not so efficient: [O(n)]
#
# @param s, a string
# @return bool
def isPalindrome(s):
    return (revertString(s) == s)

# A more efficient way is to simoultaniosly check beginning
# and end of the word until we get at the middle point. 
# This is quite efficient: [O(log(n))]
def efficientIsPalindrome(s):
    isPalindrome = True
    head = 0
    end = len(s) - 1
    while (end - head >= 1): # While the two char are not equivalent
        if (s[head] != s[end]):
            isPalindrome = False
            break
        head += 1
        end  -= 1
    return isPalindrome

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
s = "casadasac"
print("Is ", s, " a palindrome? ", efficientIsPalindrome(s))

# Efficiency testing:
longStringEven = ""
longStringOdd = ""
smallDict = {
    "Odd": "b",
    "Even": "a"
}
# I build two strings of the kind: "aaaabaaaa" so that the breaking point is in the
# middle of the string. This because this situation is the worse for my efficient
# algorithm!
# I expect it to be a palindrome if its length is ODD (e.g. "aaaaabaaaaa")
# I expect it not to be a palindrome if its lenght is EVEN (e.g. "aaaaabaaaa")

# One string with even length...
length = 15000000
for i in range(length):
    if (i == length/2):
        longStringEven += smallDict["Odd"]
    else:
        longStringEven += smallDict["Even"]
# ...one with odd length
for i in range(100001):
    if (i == (100001)/2):
        longStringOdd += smallDict["Odd"]
    else:
        longStringOdd += smallDict["Even"]

# Check for efficiency using Python time:
inefficientStart  = time.time()
inefficientResult = isPalindrome(longStringEven)
inefficientEnd    = time.time()

efficientStart  = time.time()
efficientResult = efficientIsPalindrome(longStringEven)
efficientEnd    = time.time()

print("Even length: ")
print("Inefficient result: ", inefficientResult)
print("Efficient result:   ", efficientResult)
print("Inefficient took: ", inefficientEnd - inefficientStart, " seconds")
print("Eefficient took:  ", efficientEnd - efficientStart, " seconds")
print()
print("Odd length: ")
print("Inefficient result: ", isPalindrome(longStringOdd))
print("Efficient result:   ", efficientIsPalindrome(longStringOdd))

