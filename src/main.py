from toolbox import get_toolbox
from statistics import get_statistics, get_stats_from_best_ind
from constants import NGEN, NPOP, CXPB, MUTPB
from deap import algorithms

toolbox = get_toolbox()
stats = get_statistics()
best_individual = get_stats_from_best_ind()

pop = toolbox.population(n=NPOP)
for i in pop:
    i.fitness.values = toolbox.evaluate(i)
    print(i.fitness.values)

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

print("Best ind: {}".format(best_individual[0]))
print("Fitness Value: {}".format(best_individual[0].fitness.values))
#print('Best Fit: {}'.format(evaluate(list(hal[0]))))
