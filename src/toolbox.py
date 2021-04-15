from deap import base, tools, creator
from evaluate import evaluate
from individual import create_individual

creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)

def get_toolbox():
    toolbox = base.Toolbox()
    toolbox.register('cromossome', create_individual)
    toolbox.register('individual', tools.initIterate,
                    creator.Individual, toolbox.cromossome)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)
    toolbox.register('select', tools.selTournament, tournsize=3)
    toolbox.register('mate', tools.cxOrdered)
    toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register('evaluate', evaluate)

    return toolbox