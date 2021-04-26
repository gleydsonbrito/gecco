import random
from storage import save_individual


def mate(indA, indB):
    q_points = random.randint(0, 4)
    for i in range(q_points):
        point = random.randint(0, 28)
        indA[point], indB[point] = indB[point], indA[point]
    return indA, indB
