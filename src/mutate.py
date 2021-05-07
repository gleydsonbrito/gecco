from constants import MUTPB, LOWER, UPPER
from storage import get_csv
from sklearn.cluster import KMeans
import random


def mutate(ind):
    pb = random.uniform(0, 1)
    if pb <= MUTPB:
        point = random.randint(0, 28)
        ind[point] = random.uniform(LOWER[point], UPPER[point])
    return ind,


def centroid_mutate():
    individuals = get_csv()
    cromossomes = [c[1] for c in individuals]

    kmeans = KMeans(n_clusters=6, init="k-means++")
    kmeans.fit(cromossomes)

    return kmeans
