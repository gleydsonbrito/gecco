from constants import MUTPB, LOWER, UPPER
import random


def mutate(ind):
    pb = random.uniform(0, 1)
    if pb <= MUTPB:
        point = random.randint(0, 28)
        ind[point] = random.uniform(LOWER[point], UPPER[point])
    return ind,
