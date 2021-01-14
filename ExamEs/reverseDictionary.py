# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: method
# #

# This one is faster, but it doesn't order the words alphabetically
#
# @param myDict is a python dictonary
# @return another python dictonary
def reverseDictionary(myDict):
    myItalianWords = set(myDict.keys())
    myEnglishToItalian = {}
    while (bool(myItalianWords)):
        currentItalianWord = myItalianWords.pop()
        myEnglishToItalian[myDict[currentItalianWord]] = currentItalianWord
    return myEnglishToItalian

# This one allow for dublicates. So that given a dictonary:
# {Prendere: Take, Afferrare: Take} -> {Take: [Afferrare, Prendere]}
#
# @param myDict is a python dictonary
# @return another python dictonary
def reverseDictionaryDuplicates(myDict):
    myItalianWords = set(myDict.keys())
    myEnglishToItalian = {}
    passedEnglishwords = {} # With this I remember keys passed
    for k in myDict:
        passedEnglishwords[myDict[k]] = 0 # First I set all entries to zero.
    while (bool(myItalianWords)):
        currentItalianWord = myItalianWords.pop()
        if (passedEnglishwords[myDict[currentItalianWord]] == 0):
            myEnglishToItalian[myDict[currentItalianWord]] = currentItalianWord
            passedEnglishwords[myDict[currentItalianWord]] = 1
        else:
            myEnglishToItalian[myDict[currentItalianWord]] += ", " + currentItalianWord
    return myEnglishToItalian


# ... let's make some ordering (keep in mind that sorting is really time consuming):
#
# @param myDict is a python dictonary
# @return another python dictonary
def reverseDictionaryWithOrdering(myDict):
    myItalianWords = list(myDict.keys())
    sortedEnglishToItalian = {}
    myEnglishWords = [None]*len(myItalianWords)
    i = 0
    for currentItalianWord in myItalianWords:
        myEnglishWords[i] = myDict[currentItalianWord]
        i += 1
    myEnglishWords.sort() # We need a sorted list
    unsortedEnglishToItalian = reverseDictionary(myDict) # We need the unsorted one
    for english in myEnglishWords:
        sortedEnglishToItalian[english] = unsortedEnglishToItalian[english]
    return sortedEnglishToItalian

# #
# Part 2: some testing
# #
italianToEnglish = {
    "Ciao": "Hello",
    "Come": "How",
    "Zoo": "Zoo",
    "Andare": "Go",
    "Nutella": "Nutella",
    "Bottiglia": "Bottle",
    "Libro": "Book"
}
italianToEnglishDuplex = {
    "Ciao": "Hello",
    "Come": "How",
    "Zoo": "Zoo",
    "Andare": "Go",
    "Nutella": "Nutella",
    "Bottiglia": "Bottle",
    "Libro": "Book",
    "Prendere": "Take", 
    "Afferrare": "Take"
}
print(reverseDictionary(italianToEnglish))
print(reverseDictionaryWithOrdering(italianToEnglish))
print(reverseDictionaryDuplicates(italianToEnglish))
print()
print(reverseDictionaryDuplicates(italianToEnglishDuplex))
print(reverseDictionary(italianToEnglishDuplex))
