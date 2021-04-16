from constants import MUTPB, LOWER, UPPER


def mutate(ind):
    copy_ind = ind.copy()
    pb = random.uniform(0, 1)
    if pb <= MUTPB:
        point  = random.randint(0, 29)
        copy_ind[point] = random.uniform(LOWER[point], UPPER[point])
    return copy_ind
