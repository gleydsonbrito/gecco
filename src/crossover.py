import random

def mate(indA, indB):
    iA = indA.copy()
    iB = indB.copy()
    q_points = random.randint(0, 28)
    for i in range(q_points):
        point = random.randint(0, 28)
        iA[point], iB[point] = iB[point], iA[point]

    return iA, iB
