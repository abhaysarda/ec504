import numpy as np
import math
def hashValue(data, planes):

    signature = 0
    for plane in planes:
        signature = signature << 1
        val = np.dot(plane,data)
        if val >=0:
            signature = signature | 1

    return signature

def onesCount(n):
    count = 0
    if n == 0:
        return 0
    else:
        while n:
            count += 1
            n = n & (n-1)
    return count

def angleCalc(a,b):
    prod = np.dot(a,b)
    magA = sum(a**2) ** 0.5
    magB = sum(b**2) ** 0.5
    cos = prod/magA/magB
    theta = math.acos(cos)

    return theta

dim = 3
bits = 3
run = 1
averageSimilarity = 0

for i in range(run):

    point1 = np.random.randn(dim)
    point2 = np.random.randn(dim)
    print("point1: ",point1)
    print("point2: ",point2)

    #point3 = np.array([1,1,1])

    planes = np.random.randn(bits, dim)

    sig1 = hashValue(point1, planes)
    sig2 = hashValue(point2, planes)
    print("sig1: ", sig1)
    #sig3 = hashValue(point3, planes)

    angle = angleCalc(point1,point2)
    probSameAngle = 1 - (angle/math.pi)

    probSameHash = 1 - (onesCount(sig1^sig2)/bits)

    error = (probSameAngle-probSameHash)/probSameAngle

    print("Angle: ", probSameAngle, "Hash: ", probSameHash, "Error: ", error, "%")
