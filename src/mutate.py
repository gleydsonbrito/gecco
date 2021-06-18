import random

from deap import base
from sklearn.cluster import KMeans
from scipy.spatial import distance

from constants import LOWER, UPPER
from storage import get_csv
from memory_store import all_individuals, add_inds


def mutate(ind):
    point = random.randint(0, 28)
    ind[point] = random.uniform(LOWER[point], UPPER[point])
    return ind,


def filtered_inds(mFunc):
    croms = []
    for c in mFunc():
        if c[0] <= 20.0:
            croms.append(c[1])
    return croms


def filtered_ind(ind):
    return ind[0] < 20.0


def centroid_mutate(ind):
    ind_clone = base.Toolbox().clone(ind)
    # cromossomes = [c[1] for c in get_csv()]

    # adicionei a função filtered_inds
    # para filtrar o inds com fitness < 20
    cromossomes = filtered_inds(get_csv)

    # recupera todos os individuos em memoria
    # cromossomes = [c[1] for c in all_individuals()]

    # create adaptative clusters with about 50 individuals for files CSV
    # create adaptative clusters with about 20 inds for memory inds
    n_clusters = round(len(cromossomes)/5)

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++")
    kmeans.fit(cromossomes)

    centroids = kmeans.cluster_centers_
    min_distance = float('inf')
    mutate_ind = []

    for i in range(len(centroids)):
        dist = distance.euclidean(ind_clone, centroids[i])
        if dist < min_distance:
            min_distance = dist
            mutated_ind = centroids[i]

    for i in range(len(mutated_ind)):
        ind_clone[i] = mutated_ind[i]

    return ind_clone,
