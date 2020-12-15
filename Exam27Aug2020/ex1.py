# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: methods
# #

# My task-performing method
#
# @param list1, list2 two lists of int (same length)
# @return a 2-dimensional list of strings
def getEnglishNotation(list1, list2):
    # As it is used so many times:
    l = len(list1)
    # First, I need maximum value of the two lists
    maximum = getMax(list1, list2)
    # I initialize my matrix
    outputMatrix = [[0] * l for i in range(l)]
    # To fill the matrix I need two nested for loops
    for fst in range(l):
        for snd in range(l):
            if (list2[snd] == 0 and list1[fst] == 0):
                outputMatrix[fst][snd] = getStringRepresentation(maximum)
            else:
                # Here I use string concatenation properties:
                outputMatrix[fst][snd] = getStringRepresentation(list1[fst]) + "_" + getStringRepresentation(list2[snd]) 
    return outputMatrix

# Some auxiliary functions:
def getMax(list1, list2):
    maximum = list1[0]
    # May seems too overcomplicated here but I wanted to scroll with the
    # same loop both lists (chasing speed even when not really needed :D )
    for i in range(len(list1)):
        if (list1[i] < list2[i] and maximum < list2[i]):
            maximum = list2[i]
        elif (list1[i] >= list2[i] and maximum < list1[i]):
            maximum = list1[i]
    return maximum

def getStringRepresentation(number):
    currentDictionary = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return currentDictionary[number]

# # 
# Part 2: some testing
# #

l1 = [1,0,3]
l2 = [2,5,0]
print(getEnglishNotation(l1,l2))
