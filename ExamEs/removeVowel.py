# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1 (function)
# #

# My task-performing method:
#
# @param word is a string, subs a char
# @return a string
def removeVowel(word, subs):
    isSubsAVowel = isAVowel(subs)
    outputString = ""
    if (isSubsAVowel):
        outputString = performWithChange(word, subs)
    else:
        outputString = performWithDelete(word)
    outputString = countConsonant(outputString)
    return outputString

# I change every voewl to X:
#
# @param string is a string, x a char
# @return a string
def performWithChange(string, x):
    outputString = ""
    for i in range(len(string)):
        if (isAVowel(string[i])):
            outputString += x
        else:
            outputString += string[i]
    return outputString

# I delete every voewl:
#
# @param string is a string
# @return a string
def performWithDelete(string):
    outputString = ""
    for i in range(len(string)):
        if (isAVowel(string[i])):
            outputString += ""
        else:
            outputString += string[i]
    return outputString

# Count consonant:
#
# @param string is a string
# @return a string
def countConsonant(string):
    outputString = ""
    i = 0
    while (i < len(string)):
        count = 1
        k = i+1
        while (k < len(string) and string[k] == string[i] and isAVowel(string[i]) == False):
            i += 1
            k += 1
            count += 1
        if (count > 1):
            outputString += string[i]
            outputString += str(count)
        else:
            outputString += string[i]
        i += 1
    return outputString


# Method to know whether a char is a vowel or not:
#
# @param char is a char
# @return bool
def isAVowel(char):
    isCharAVowel = False
    asciiCodes = [65, 69, 73, 79, 85]
    for code in asciiCodes:
        if (ord(char) == code or ord(char) == code + 32):
            isCharAVowel = True
            break
    return isCharAVowel

# #
# Part 2: some testing 
# #
print("I expect b2:")
print(removeVowel("aabba", "k"))
print("I expect iib2i:")
print(removeVowel("aabba", "i"))
print("I expect null:")
print(removeVowel("aaa", "k"))
print("I expect ooooob5oor3ooo:")
print(removeVowel("aeioubbbbbaerrruiu", "o"))

