import random
from storage import save_individual
from deap import base


def mate(indA, indB):
    copy_a = base.Toolbox().clone(indA)
    copy_b = base.Toolbox().clone(indB)

    q_points = random.randint(0, 28)

    for i in range(q_points):
        gene_position = random.randint(0, 28)
        copy_a[gene_position], copy_b[gene_position] = copy_b[gene_position], copy_a[gene_position]

    return copy_a, copy_b
