# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: functions
# #

# My task-performing method:
# time complexity O(n^2) :'(
#
# @param matrix
# @return matrix
def transposeMatrix(M):
    r, c = getDimensions(M)
    outputMatrix = [[0] * r for i in range(c)]
    for i in range(r):
        for j in range(c):
            outputMatrix[j][i] = M[i][j]
    return outputMatrix

def getDimensions(M):
    row = len(M)
    col = len(M[0])
    return row, col

# #
# Part 2: some testing
# #
def printMatrixProperly(M):
    r, _ = getDimensions(M)
    for i in range(r):
        print(M[i])
    print()

A = [[1,2,3,4,5],[6,7,8,9,0]]
At = transposeMatrix(A)
B = [["a","b","c"], ["d","e","f"], ["g", "h", "i"]]
Bt = transposeMatrix(B)
print("A is: ")
printMatrixProperly(A)
print("A transpose is: ")
printMatrixProperly(At)
print("B is: ")
printMatrixProperly(B)
print("B transpose is: ")
printMatrixProperly(Bt)