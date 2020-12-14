# #
# Part 1:  methods
# #

# I want to implement this method scrolling
# the two lists at the same time. And just once!!
def mergeWithOddsFirst(list1, list2):
    # I create an auxiliary vector
    merged = [None] * (len(list1)*2)
    end = (len(list1)*2) - 1
    beginning = 0
    for i in range(len(list1)):
        if (isEven(list1[i])):
            merged[end] = list1[i]
            end -= 1
        else:
            merged[beginning] = list1[i]
            beginning += 1
        if (isEven(list2[i])):
            merged[end] = list2[i]
            end -= 1
        else:
            merged[beginning] = list2[i]
            beginning += 1
    return merged

# A useful auxiliary method:
def isEven(n):
    if (n%2 == 0):
        return True
    else:
        return False

# #
# Part 2: some testing:
# #
a = [2,2,3,4,6,2]
b = [1,4,2,2,2,3]
print(mergeWithOddsFirst(a, b))