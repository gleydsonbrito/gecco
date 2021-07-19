import random

import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
from deap import tools, base, creator

from mutate import filtered_inds
from storage import save_individual, get_csv
from memory_store import all_individuals, add_inds


def mate(indA, indB):
    """Function to crossover two individuals. Part of evolutionary process.
    :params indA: the first individual to crossover
    :params indB: the second indivitual to crossover
    :return : This function return two childrens created by parents indA 
    and indB.
    First will be calculated the probability to use the centroid_mate
    operator. If no use this operator, the algorthm goes to the normal
    operator. First we copy the inds A and B. Before generate a aleatory 
    quantity numbers between 1 and 29 and for all numbers calculate the gene
    that will be chaged. The gene chosed will be permuted between individuals.
    """

    # Cada ind tem 15% de chance de efetuar o cruzamento baseado em centroide
    # a partir dos indivíduos com aptidão menores que 20.000
    # quando a probabilidade está 0.0 não se considera a função centroid_mate
    if random.random() < 0.15:
        return centroid_mate(indA, indB)

    copy_a = base.Toolbox().clone(indA)
    copy_b = base.Toolbox().clone(indB)

    q_points = random.randint(0, 28)

    for i in range(q_points):
        gene_position = random.randint(0, 28)
        copy_a[gene_position], copy_b[gene_position] = copy_b[gene_position], copy_a[gene_position]

    return copy_a, copy_b


def centroid_mate(indA, indB):
    """Crossover two inds by centroid operator.
    :params indA: first ind to crossover
    :params indB: second ind to crossover
    :return : A generated individual by two parents
    First create a copy of two inds. Retrive all of individual stored in
    memory or csv file. Create a number of cluster, dinamic or
    deterministicly. Get the virtual ind by :meth:get_closer_ind. After
    merge two childrens by :meth:merge. Return two childrens created.
    :meth:filtered_inds apply filter when we use the inds stored in CSV file.
    """
    copy_a = base.Toolbox().clone(indA)
    copy_b = base.Toolbox().clone(indB)

    # usando arquivo CSV
    individuals = filtered_inds(get_csv)

    # usando memoria
    # individuals = [c[1] for c in all_individuals()]

    # create adaptative clusters with about 20 individuals
    n_clusters = round(len(individuals)/10)

    # use 5 quando for com memória
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++")
    kmeans.fit(individuals)

    centroids = kmeans.cluster_centers_

    closer_a = get_closer_ind(indA, centroids)
    closer_b = get_closer_ind(indB, centroids)

    copy_a = merge(indA, closer_a)
    copy_b = merge(indB, closer_b)

    return copy_a, copy_b


def get_closer_ind(ind, centroids):
    """This function get the centroid closest to individual.
    :params ind: individual to crossover
    :params centroids: list of centroids of all clusters
    :return : A virtual individual closest of a individual.
    To find the virtual individual (centroid) closest of individual,
    cheking all of centroids by euclidean distance. After, copy the cromossome
    of a virtual individual to generated individual by cloning.
    """
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
    """ Create a child by two parents merging your cromossomes.
    :params indA: first ind to merge
    :params indB: second ind to merge
    :return : An individual with cromossome merging by two parents.
    Each gene has a probability 50% to go of the first or second parent.
    """
    children = base.Toolbox().clone(indA)
    for i in range(len(children)):
        rnd = random.uniform(0, 1)
        if rnd <= 0.5:
            children[i] = indB[i]

    return children
