from deap import tools

from constants import NPOP


def ranking_selection(pop):
    """Function to seletc individuals by fitness. Use the roulette
    selectiton to create a selection relative to fitness.
    :params pop: total of individuas in a generation
    :returns : the offspring that allways contain the best individual.
    """
    k = len(pop)-2
    best_ind = tools.selBest(pop, 1)
    k_worst_individuals = tools.selWorst(pop, k)
    offspring = tools.selRoulette(k_worst_individuals, NPOP-1)

    return best_ind + offspring
