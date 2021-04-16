import random
from constants import LOWER, UPPER

def create_individual():
    candiadate_solution = []
    for k in range(29):
        candiadate_solution.append(random.uniform(LOWER[k], UPPER[k]))
    return candiadate_solution
