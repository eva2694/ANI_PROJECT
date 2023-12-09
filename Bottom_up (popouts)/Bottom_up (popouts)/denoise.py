import pandas as pd
from sklearn.neighbors import NearestNeighbors


def remove_outliers_knn(points, k=3, min_connections=2, max_iter=3):
  knn = NearestNeighbors(n_neighbors=k)

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_counts = knn.kneighbors_graph(points.values).toarray().sum(axis=0)
    points_to_keep = [points.iloc[i] for i, connections in enumerate(connection_counts) if
                      connections >= min_connections]

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = pd.concat(points_to_keep, axis=1).T

  return points_to_keep


def remove_outliers_radius(points, radius=10, min_connections=2, max_iter=3):
  knn = NearestNeighbors(radius=radius)

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_counts = knn.radius_neighbors_graph(points.values).toarray().sum(axis=0)
    points_to_keep = [points.iloc[i] for i, connections in enumerate(connection_counts) if
                      connections >= min_connections]

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = pd.concat(points_to_keep, axis=1).T

  return points_to_keep
