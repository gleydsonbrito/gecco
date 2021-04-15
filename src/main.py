from toolbox import get_toolbox
from statistics import get_statistics, get_best_individual
from deap import algorithms, tools
import random as rd
import numpy as np

NGEN = 10
NPOP = 20
CXPB, MUTPB = 0.7, 0.03

toolbox = get_toolbox()
stats = get_statistics()
best_individual = get_best_individual()

pop = toolbox.population(n=NPOP)
for i in pop:
    i.fitness.values = toolbox.evaluate(i)

algorithms.eaSimple(
    pop,
    toolbox,
    cxpb=CXPB,
    mutpb=MUTPB,
    ngen=NGEN,
    stats=stats,
    halloffame=best_individual,
    verbose=True
)

print(hal[0])
print('Best Fit ', evaluate(list(hal[0])))
