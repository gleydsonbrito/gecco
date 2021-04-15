from evaluate import evaluate
from individual import create_individual
from deap import base, creator, tools, algorithms
import random as rd
import numpy as np
import array
import json
import time

NGEN = 10
NPOP = 20
CXPB, MUTPB = 0.7, 0.03


# cria as classes
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register('cromossome', create_individual)
toolbox.register('individual', tools.initIterate,
                 creator.Individual, toolbox.cromossome)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('select', tools.selTournament, tournsize=3)
toolbox.register('mate', tools.cxOrdered)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.05)
toolbox.register('evaluate', evaluate)


pop = toolbox.population(n=NPOP)
for i in pop:
    i.fitness.values = toolbox.evaluate(i)

hal = tools.HallOfFame(1)

stats = tools.Statistics(lambda ind: ind.fitness.values)

stats.register('avg', np.mean)
stats.register('std', np.std)
stats.register('min', np.min)
stats.register('max', np.max)

algorithms.eaSimple(
    pop,
    toolbox,
    cxpb=CXPB,
    mutpb=MUTPB,
    ngen=NGEN,
    stats=stats,
    halloffame=hal,
    verbose=True
)

print(hal[0])
print('Best Fit ', evaluate(list(hal[0])))
