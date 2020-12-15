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
print(reverseDictionary(italianToEnglish))
print(reverseDictionaryWithOrdering(italianToEnglish))
