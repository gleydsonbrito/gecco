import random
from constants import LOWER, UPPER

def create_individual():
    for i in range(2):
        candiadate_solution = []
        for k in range(29):
            candidateSolution.append(random.uniform(LOWER[k], UPPER[k]))
    
    return candiadate_solution
