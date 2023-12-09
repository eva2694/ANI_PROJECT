import pandas as pd
from sklearn.neighbors import NearestNeighbors


def remove_outliers_knn(points, k=3):
  knn = NearestNeighbors(n_neighbors=k)

  while True:
    knn.fit(points.values)
    connection_counts = knn.kneighbors_graph(points.values).toarray().sum(axis=0)
    points_to_keep = [points.iloc[i] for i, connections in enumerate(connection_counts) if connections >= 2]

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = pd.concat(points_to_keep, axis=1).T
