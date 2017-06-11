from typing import Tuple, Iterable, Sequence, List, Dict, DefaultDict
from random import sample
from math import fsum, sqrt
from collections import defaultdict

def partial(func, *args):
    "Rewrite functools.partial() in a way that doesn't confuse mypy"
    def inner(*moreargs):
        return func(*args, *moreargs)
    return inner

def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)

def transpose(matrix: Iterable[Iterable]) -> Iterable[tuple]:
    'Swap rows with columns for a 2-D array'
    return zip(*matrix)

Point = Tuple[float, ...]
Centroid = Point

def dist(p: Point, q: Point, sqrt=sqrt, fsum=fsum, zip=zip) -> float:
    'Multi-dimensional euclidean distance'
    return sqrt(fsum((x1 - x2) ** 2.0 for x1, x2 in zip(p, q)))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, Sequence[Point]]:
    'Assign data the closest centroid'
    d : DefaultDict[Point, List[Point]] = defaultdict(list)
    for point in data:
        centroid: Point = min(centroids, key=partial(dist, point))
        d[centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    'Compute the centroid of each group'
    return [tuple(map(mean, transpose(group))) for group in groups]

def k_means(data: Iterable[Point], k:int=2, iterations:int=10) -> List[Point]:
    'Return k-centroids for the data'
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids

def quality(labeled: Dict[Centroid, Sequence[Point]]) -> float:
    'Mean value of squared distances from data to its assigned centroid'
    return mean(dist(c, p) ** 2 for c, pts in labeled.items() for p in pts)


if __name__ == '__main__':

    from pprint import pprint

    print('Simple example with six 3-D points clustered into two groups')
    points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]

    centroids = k_means(points, k=2)
    pprint(assign_data(centroids, points))

    print('\nExample with a richer dataset.')
    print('See: https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials')

    data = [
         (10, 30),
         (12, 50),
         (14, 70),

         (9, 150),
         (20, 175),
         (8, 200),
         (14, 240),

         (50, 35),
         (40, 50),
         (45, 60),
         (55, 45),

         (60, 130),
         (60, 220),
         (70, 150),
         (60, 190),
         (90, 160),
    ]

    print('k     quality')
    print('-     -------')
    for k in range(1, 8):
        centroids = k_means(data, k, iterations=20)
        d = assign_data(centroids, data)
        print(f'{k}    {quality(d) :8,.1f}')
