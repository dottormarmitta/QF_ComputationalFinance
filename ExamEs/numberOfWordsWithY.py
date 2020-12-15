# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: methods
# #

# My task-performing method
#
# @param sentence, a string
# @return a integer
def numberOfWordsWithY(sentence):
    numberOfWords = 0
    for i in range(len(sentence)):
        if (sentence[i] == "y" or sentence[i] == "Y"):
            if (i+1 < len(sentence) and sentence[i+1] == " "):
                numberOfWords += 1
            elif (i == len(sentence) - 1):
                numberOfWords += 1
    return numberOfWords

# #
# Part 2: some testing
# #
mySentence = "Today I went to a party and saw Jimmy"
# I expect 3
print(numberOfWordsWithY(mySentence))
whileIamCrazy = "yyyyy yyyyy uuuY"
# Again, I expect 3:
print(numberOfWordsWithY(whileIamCrazy))