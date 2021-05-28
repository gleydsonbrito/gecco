import random

import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
from deap import tools, base, creator

from mutate import filtered_inds
from storage import save_individual, get_csv


def mate(indA, indB):
    # Cada ind tem 30% de chance de efetuar o cruzamento baseado em centroide
    # a partir dos indivíduos com aptidão menores que 20.000
    if random.random() < 0.3:
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

    #individuals = [c[1] for c in get_csv()]
    # recupera os indivíduos com fitness abaixo de 20 para montar os clusters
    individuals = filtered_inds(get_csv)

    # create adaptative clusters with about 20 individuals
    n_clusters = round(len(individuals)/50)

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++")
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
        if rnd >= 0.5:
            children[i] = indB[i]

    return children


def sgd_mate(indA, indB, population):
    k_best_inds = tools.selBest(population, 20)
    group_a = k_best_inds[:4]
    group_b = k_best_inds[5:]

    centroid_a = creator.Individual(np.mean(group_a))
    centroid_b = creator.Individual(np.mean(group_b))

    ind_a = merge(indA, centroid_a)
    ind_b = merge(indB, centroid_b)

    return ind_a, ind_b
