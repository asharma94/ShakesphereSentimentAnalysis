import math
import random
import numpy as np
from scipy import integrate


# c1,c2 are lists of values w/ same length
def character_distance(c1, c2, method="simpson"):
    if len(c1) != len(c2):
        raise ValueError("Characters arrays not same length!")

    abs_diff = []

    for i in range(len(c1)):
        abs_diff.append(abs(c1 - c2))

    if method is "simpson":
        dist = integrate.simps(abs_diff, dx=1)
    elif method is "trapz":
        dist = np.trapz(abs_diff, dx=1)
    else:
        raise ValueError("Invalid method param given")

    return dist

# chars is dict of characters, centers is list of k centers
# returns array of length k, k is kth center and array element
# array of character names (strings) closest to that center
def char_clusters(chars, centers):
    res = [[] for i in range(len(centers))]
    for charName, charPoints in chars.items():
        shortestDist = character_distance(charPoints, centers[0])
        closestCenter = 0
        for i in range(1, len(centers)):
            d = character_distance(centers[i], charPoints)
            if d < shortestDist:
                shortestDist = d
                closestCenter = i
        res[closestCenter].append(charName)
    return res


def calculate_centers(chars, clusters):
    centers = []
    for cl in clusters:
        cent = [chars[name] for name in cl] # a list of lists of points of characters in cl
        cent = [sum(x) for x in zip(*cent)]
        cent = map(lambda m: float(m)/len(cl), cent)
        centers.append(cent)
    return centers


# chars is dict with only numbers in columns i.e. distance function
# is square root of sum of squares of columns
# returns: list of k tuples representing clusters which hold (centerlist, charnames)
def characterKMeans(chars, k, max_iter=100):
    cent_keys = np.random.choice(chars.keys(), shape=k)
    centers = []
    for k in cent_keys:
        centers.append(chars[k])

    for it in range(max_iter):
        clusters = char_clusters(chars, centers)
        centers = calculate_centers(chars, clusters)
    final_clusters = char_clusters(chars, centers)
    final_centers = calculate_centers

    return zip(final_centers, final_clusters)