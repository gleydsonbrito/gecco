import random
from evaluate import evaluate

lower = [6, 7, 3, 3, 3, 5, 3, 3, 25, 17, 2, 1, 0.25, 0.05, 0.07, 0.005,
         0.07, 1e-04, 0.08, 0.25, 0.08, 0.5, 1e-06, 2, 1e-06, 1e-06, 1, 2, 0.5]
upper = [14, 13, 7, 9, 7, 9, 5, 7, 35, 25, 5, 7, 2, 0.15, 0.11, 0.02,
         0.13, 0.002, 0.12, 0.35, 0.12, 0.9, 0.01, 4, 1.1, 0.0625, 2, 5, 0.75]


def create_individual():
    for i in range(2):
        candidateSolution = []
        for k in range(29):
            candidateSolution.append(random.uniform(lower[k], upper[k]))

    print(candidateSolution)
    ev = evaluate(candidateSolution)
    print(ev)


createIndividual()
