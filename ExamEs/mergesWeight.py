# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: methods
# #

# My task-performing method
#
# @param strings is a list of strings
# @return sorted list by weight
def mergesW(strings):
    # I store string and their weight in a dictonary.
    # Keys are the weight, value the strings
    # So this is like {4: "e", 10: "age", ...}
    myWeightedString = {}
    for currentWord in strings:
        myWeightedString[getWeight(currentWord)] = currentWord
    myWeights = list(myWeightedString.keys())
    myWeights.sort() # "I" just sort the keys: one line but very time consuming!!!
    sortedList = [None]*len(strings)
    for i in range(len(strings)):
        sortedList[i] = myWeightedString[myWeights[i]]
    return sortedList

# Method to get string weight:
#
# @param myString is a string
# @return integer containing weight
def getWeight(myString):
    localString = myString.lower()
    weight = 0
    for i in range(len(myString)):
        weight += ord(localString[i])-97 # See ASCII table why this 96
    return weight

# #
# Part 2: some testing
# #
myCurrentList = ["AAAA", "bbbb", "aaba", "bbba", "caaa", "Z", "dded"]
print(mergesW(myCurrentList))

