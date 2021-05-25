from constants import LOWER, UPPER
from deap import base
from storage import get_csv
from sklearn.cluster import KMeans
from scipy.spatial import distance
import random


def mutate(ind):
    point = random.randint(0, 28)
    ind[point] = random.uniform(LOWER[point], UPPER[point])
    return ind,


def centroid_mutate(ind):
    ind_clone = base.Toolbox().clone(ind)
    cromossomes = [c[1] for c in get_csv()]

    # create adaptative clusters with about 200 individuals
    n_clusters = round(len(cromossomes)/200)

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


# mut = centroid_mutate([6.815736838193935, 11.66095896456695, 5.890178907164971, 3.7102530295496177, 6.070594996464887, 7.403798774843138, 3.694358678086288, 3.56187077108757, 34.566743841688805, 23.660429548127897, 3.6600788353571154, 6.815460134330752, 1.8776378942214158, 0.10704545213839409,
#                        0.09501376922236714, 0.01666207407361643, 0.12284435086362626, 0.001969933160091152, 0.08383424707133179, 0.3482460098670257, 0.11807448413129469, 0.6401878630861229, 0.003723697952887368, 3.7731433506168774, 0.9124103412691668, 0.06116595456316067, 1.259443125795108, 2.775846595652113, 0.69744733900394])

# print(mut)
# print(mut.fitness.value)
