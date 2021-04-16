form deap import tools
import numpy as np

def get_statistics():
    stats = tools.Statistics(lambda ind: ind.fitness.values)

    stats.register('avg', np.mean)
    stats.register('std', np.std)
    stats.register('min', np.min)
    stats.register('max', np.max)

    return stats

def get_best_individual():
    hal = tools.HallOfFame(1)
    return hal