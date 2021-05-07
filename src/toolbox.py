from deap import base, tools, creator
from evaluate import evaluate
from individual import create_individual
from crossover import mate
from mutate import mutate, centroid_mutate

creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)


def get_toolbox():
    toolbox = base.Toolbox()
    toolbox.register('cromossome', create_individual)
    toolbox.register('individual', tools.initIterate,
                     creator.Individual, toolbox.cromossome)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)
    toolbox.register('select', tools.selTournament, tournsize=3)
    toolbox.register('mate', mate)
    toolbox.register('mutate', centroid_mutate)
    toolbox.register('evaluate', evaluate)

    return toolbox
