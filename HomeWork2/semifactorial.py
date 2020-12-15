# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: functions
# #

# Task-performing function
#
# @param n is an integer
# @return integer
def semifactorial(n):
    if (n > 1):
        return n*semifactorial(n-2)
    return 1

# #
# Part 2: some testing
# #
n = 7
print(semifactorial(n))