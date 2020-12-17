# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: functions
# #

# My task-performing method:
#
# @param n, an integer
# @return an integer
def recursionFactorial(n):
    # If you want to prevent float errors: n = int(n)
    if n > 0:
        return n*recursionFactorial(n-1)
        # n! = 1*2*...*(n-1)*n = (n-1)!*n
    else:
        return 1

# #
# Part 2: some testing
# #
a = 3
print(recursionFactorial(a))