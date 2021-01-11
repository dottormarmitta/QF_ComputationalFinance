# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com


# #
# Part 1 (function)
# #

# My task-performing method:
#
# @param sentence, word are strings
# @return a list of string
def getListWithWordsContainingLetters(sentence, word):
    word = word.lower()
    i = 0
    outputList = []
    while (i < len(sentence)):
        letterDict = getEvenDictionary(word)
        k = i
        while i < len(sentence) and isALetter(sentence[i]):
            letterDict[sentence[i].lower()] = 1
            i += 1
        if (getSum(letterDict) == len(letterDict)):
            outputList.append(sentence[k:i])
        i += 1
    return outputList

def isALetter(c):
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False

def getEvenDictionary(string):
    outputDict = {}
    for i in range(len(string)):
        if (i%2 == 0):
            outputDict[string[i]] = 0
    return outputDict

def getSum(dictonary):
    sum = 0
    for v in dictonary:
        sum += dictonary[v]
    return sum


# #
# Part 2: some testing 
# #
s = "AbraCadabrae may my dREams coMe true! MaYbe this time for Real. YeS!!"
w1 = "aLe"
print("I expect to have: 'AbraCadabra', 'dReams', 'MaYbe', 'Real': ")
print(getListWithWordsContainingLetters(s, w1))
print()
w2 = "MAy"
print("I expect to have: 'may', 'my', 'MaYbe': ")
print(getListWithWordsContainingLetters(s, w2))