# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: functions
# #

# My task-performing method:
#
# @param list1, list2 are two lists of same length
# it works elementwise
# @return list of variable length
def multiplyAndRemoveOdd(list1, list2):
    outputList =[]
    localMult = 0
    for i in range(len(list1)):
        localMult = list1[i]*list2[i]
        if isEven(localMult):
            outputList.append(localMult)
    return outputList

#
def isEven(n):
    if (n%2 == 0):
        return True
    return False

# #
# Part 2: some testing
# #
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(multiplyAndRemoveOdd(list1, list2))