# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: methods
# #

# § Throughout cartesian point is represented as a list p = [xp, yp]

# My task-performing method
#
# @param three cartesian points §see above§
# @return float
def biggestCirclePerimeter(c, p1, p2):
    # where I have c = [xc, yc], p1 = [xp1, yp1], p2 = [xp2, yp2]
    ray1 = getDistance(c, p1)
    ray2 = getDistance(c, p2)
    pi = 3.14159265358979323846264338327950288
    maxRay = getMaximum(ray1, ray2)
    return 2*pi*maxRay

# Auxiliary methods:
def getDistance(p, q):
    # Sqrt((xq - xp)^2 + (yq - yp)^2)
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2)**0.5

def getMaximum(a, b):
    if (a > b):
        return a
    return b

# #
# Part 2: some testing
# #
P = [0, 3]
C = [0, 0]
Q = [1, 1]
print(biggestCirclePerimeter(C,P,Q))