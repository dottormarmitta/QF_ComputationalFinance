# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: methods
# #

def getWeight(s):
    i = 0
    j = 2
    weight = 0
    while (j < len(s)):
      if (isAVowel(s[i]) and isAVowel(s[j]) and not isAVowel(s[i+1])):
          weight += 1
      i += 1
      j += 1  
    return weight  

def isAVowel(char):
    isCharAVowel = False
    asciiCodes = [65, 69, 73, 79, 85]
    for code in asciiCodes:
        if (ord(char) == code or ord(char) == code + 32):
            isCharAVowel = True
            break
    return isCharAVowel

# IF you DO NOT want to change the original matrix,
# uncomment lines 31 and 34. Comment line 33!
def findN(Matrix, N):
    output = ""
    #newMatrix = [row[:] for row in Matrix]
    for _ in range(N):
        output += getMaxAndChange(Matrix)
        #output += getMaxAndChange(newMatrix)
    return output

# TO BE NOTED: this method changes DIRECTLY and PERMANENTLY A
def getMaxAndChange(A):
    weightMax = 0
    row       = 0
    col       = 0
    wordMax   = ""
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (getWeight(A[i][j]) > weightMax):
                weightMax = getWeight(A[i][j])
                wordMax   = A[i][j]
                row = i
                col = j
    A[row][col] = 'no val.'
    return wordMax
        
# # 
# Part 2: some testing
# #

s = "ratataplan"
print(getWeight(s))
M = [["ratataplan", "acehice", "acehuce"], ["hulilla", "hell", "didid"], ["uto", "ito", "ato"]]
print(findN(M, 2))
print(M)