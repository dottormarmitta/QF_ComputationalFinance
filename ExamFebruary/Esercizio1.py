# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# PART 1: build the program
# #

# Firts, I would define some auxiliary methods:
def addIfNecessary(s: str):
    """
    This method adds "$" until the length of the string
    becomes divisible by three!
    """
    while (len(s)%3 != 0):
        s += "$"
    return s

def breakString(s: str):
    """
    Given a string whose length is multiple of three, it
    returns its division in three parts!
    """
    individualStrings = ["", "", ""]
    lengthOfString = int(len(s)/3)
    for i in range(lengthOfString):
        individualStrings[0] += s[i]
        individualStrings[1] += s[i + lengthOfString]
        individualStrings[2] += s[i + 2*lengthOfString]
    return individualStrings

def mergeThreeString(s1: str, s2: str, s3: str):
    """
    Given three strings of same length, it returns their
    merges according to the rule defined!
    """
    listOfTuples = []
    for i in range(len(s1)):
        currentTuple = [s1[i], s2[i], s3[i]]
        currentTuple.sort() # This line is so sad :'(
        listOfTuples.append(tuple(currentTuple))
    return listOfTuples

# Task-performing methods:
def main(bigString: str):
    """
    Just the one called on the input given!
    """
    theThreeWords = breakString(addIfNecessary(bigString))
    print(mergeThreeString(theThreeWords[0],theThreeWords[1],theThreeWords[2]))

# #
# PART 2: some testing
# #

# Trial:
myString = "GiveMeAnything"
main(myString)
print(myString)