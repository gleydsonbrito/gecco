import random

import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
from deap import tools, base, creator

from mutate import filtered_inds
from storage import save_individual, get_csv
from memory_store import all_individuals, add_inds


def mate(indA, indB):
    """Function to crossover two individual. Part of evolutionary process.
    :params indA: the first individual to crossover
    :params indB: the second indivitual to crossover
    :return : This function return two childrens created by two parents indA 
    and indB.
    First will be calculated the probability to use the centroid_mate
    operator. If no use this operator, the algorthm goes to the normal
    operator. First we copy the inds A and B. Before generate a aleatory 
    quantity numbers between 1 and 29 and for all numbers calculate the gene
    that will be chaged. The gene chosed will be permuted between individuals.
    """

    # Cada ind tem 30% de chance de efetuar o cruzamento baseado em centroide
    # a partir dos indivíduos com aptidão menores que 20.000
    if random.random() < 0.4:
        return centroid_mate(indA, indB)

    copy_a = base.Toolbox().clone(indA)
    copy_b = base.Toolbox().clone(indB)

    q_points = random.randint(0, 28)

    for i in range(q_points):
        gene_position = random.randint(0, 28)
        copy_a[gene_position], copy_b[gene_position] = copy_b[gene_position], copy_a[gene_position]

    return copy_a, copy_b


def centroid_mate(indA, indB):
    copy_a = base.Toolbox().clone(indA)
    copy_b = base.Toolbox().clone(indB)

    # individuals = [c[1] for c in get_csv()]
    # recupera os indivíduos com fitness abaixo de 20 para montar os clusters
    # usando arquivo CSV
    # individuals = filtered_inds(get_csv)

    # usando memoria
    individuals = [c[1] for c in all_individuals()]

    # create adaptative clusters with about 20 individuals
    n_clusters = round(len(individuals)/20)

    # use 5 quando for com memória
    kmeans = KMeans(n_clusters=5, init="k-means++")
    kmeans.fit(individuals)

    centroids = kmeans.cluster_centers_

    closer_a = get_closer_ind(indA, centroids)
    closer_b = get_closer_ind(indB, centroids)

    copy_a = merge(indA, closer_a)
    copy_b = merge(indB, closer_b)

    return copy_a, copy_b


def get_closer_ind(ind, centroids):
    min_distance = float('inf')
    closer_ind = base.Toolbox().clone(ind)
    temp_ind = []

    for i in range(len(centroids)):
        dist = distance.euclidean(ind, centroids[i])
        if dist < min_distance:
            min_distance = dist
            temp_ind = centroids[i]

    for i in range(len(temp_ind)):
        closer_ind[i] = temp_ind[i]

    return closer_ind


def merge(indA, indB):
    children = base.Toolbox().clone(indA)
    for i in range(len(children)):
        rnd = random.uniform(0, 1)
        if rnd <= 0.5:
            children[i] = indB[i]

    return children

# essa abordagem foi abortada


def sgd_mate(indA, indB, population):
    k_best_inds = tools.selBest(population, 20)
    group_a = k_best_inds[:4]
    group_b = k_best_inds[5:]

    centroid_a = creator.Individual(np.mean(group_a))
    centroid_b = creator.Individual(np.mean(group_b))

    ind_a = merge(indA, centroid_a)
    ind_b = merge(indB, centroid_b)

    return ind_a, ind_b
